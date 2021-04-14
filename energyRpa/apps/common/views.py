import json
import requests
import xmltodict

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt

from apps.calculator.models import CalcUvalueTmpl
from apps.common.models import CmnProject
from apps.common.models import CmnAreaGb
from apps.common.models import CmnPurps


def index(request):
    return render(request, 'index.html')

def signin(request):
    try:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
    except (KeyError, username == "", password == ""):
        return render(request, {"result": False, "message": "아이디와 비밀번호를 모두 입력하세요."})
    else:
        auth = authenticate(username=username, password=password)
        if auth is not None:
            if auth.is_active:
                request.session['username'] = auth.username
                context = {"result": True}
            else:
                context = {"result": False, "message": "사용 중지 된 계정입니다."}
        else:
            context = {"result": False, "message": "아이디 또는 비밀번호를 확인하세요."}
        return HttpResponse(json.dumps(context), content_type="application/json")

def list(request):
    username = request.session.get('username')
    calc_list = CalcUvalueTmpl.objects.filter(username=username)
    print(str(calc_list.query))
    context = {"calc_list": calc_list}
    return render(request, 'list.html', context)

@csrf_exempt
def insert_project(request):
    # POST 요청이면 최초 프로젝트 정보를 저장한다
    if request.method == 'POST':
        # 모델 객체 생성
        project = CmnProject()

        # 클라이언트에서 보낸 주소 데이터 파싱
        data = json.loads(request.body)

        # 클라이언트에서 보낸 주소 데이터 → 도로명주소, 시군구코드, 법정동코드, 필지고유번호(pnu), 지역구분 Model Set, 사용자정보
        project.road_address = data['road_address']
        project.sigungu_cd = data['sigungu_cd']
        project.bjdong_cd = data['bjdong_cd']
        project.pnu = data['pnu']
        project.area_gb_cd = data['area_gb_cd']
        project.username = request.session['username']

        # 건축물대장 표제부 API call → 대지면적, 연면적, 건폐율, 주용도명, 주용도코드 Model Set
        host = "http://apis.data.go.kr/1613000/BldRgstService_v2/"
        serviceKey = 'ao%2FcmGTqY3iWzbRNwgrbiO%2BJOl1GzDNAAVTbiH6%2BcEFGTm0MF6P5pFH3ZzkC5BEhScoQnj2rU3LVS0Dc5blLZw%3D%3D'
        operation = 'getBrTitleInfo'   # 건축물대장 표제부
        params = "?sigunguCd=" + data['sigungu_cd'] + "&bjdongCd=" + data['bjdong_cd'] + "&bun=" + data['bun'] + "&ji=" + data['ji'] + "&ServiceKey=" + serviceKey
        url = host + operation + params
        try:
            res = requests.get(url)
            if res.status_code == 200:
                print(res.url)
                res_data = xml_to_dict(res.text).get('response').get('body').get('items').get('item')
                project.plat_area = res_data.get('platArea')
                project.tot_area = res_data.get('totArea')
                project.tot_area = res_data.get('totArea')
                project_nm = data['bname'] + " " + res_data.get('etcPurps').split(',')[0]   # 프로젝트명 = 읍면동 + 건축물 주용도
                project.project_nm = project_nm
                purps_nm = res_data.get('mainPurpsCdNm')
                project.purps_nm = purps_nm
                '''
                용도코드 임시로 구분(단독주택,공동주택-주거,그 외-비주거)
                향후 주용도코드로 관리해야함
                '''
                if purps_nm == "단독주택" or purps_nm == "공동주택":
                    project.purps_cd = 0
                else:
                    project.purps_cd = 1
        except Exception as e:
            print(e)

        # 건축물대장 지역지구구역 API call →  지역지구구역코드명 Model Set
        operation = 'getBrJijiguInfo'   # 건축물대장 지역지구구역
        url = host + operation + params
        try:
            res = requests.get(url)
            if res.status_code == 200:
                print(res.url)
                res_data = xml_to_dict(res.text).get('response').get('body').get('items').get('item')
                project.jijigu_cd_nm = res_data.get('jijiguCdNm')
        except Exception as e:
            print(e)

        # 토지임야목록 API call →  지목명 Model Set lndcgrCodeNm
        url = "http://openapi.nsdi.go.kr/nsdi/eios/LadfrlService/ladfrlList.xml"
        authkey = '95d5aa9d0cae5aaf12ba73'
        url += "?pnu=" + data['pnu'] + "&authkey=" + authkey
        try:
            res = requests.get(url)
            if res.status_code == 200:
                print(res.url)
                res_data = xml_to_dict(res.text).get('fields').get('ladfrlVOList')
                project.lndcgr_code_nm = res_data.get('lndcgrCodeNm')
        except Exception as e:
            print(e)
        
        # 프로젝트 초기 데이터 DB 저장
        project.save()
        project_cd = CmnProject.objects.order_by('-pk')[0].project_cd
        context = {"result": True, "project_cd": project_cd}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {"result": False}
        return HttpResponse(json.dumps(context), content_type="application/json")

def xml_to_dict(xml_text) :
    return json.loads(json.dumps(xmltodict.parse(xml_text)))

def select_project(request, project_cd):
    project = CmnProject.objects.filter(project_cd=project_cd)
    print(str(project.query))
    area = CmnAreaGb.objects.all()
    use = CmnPurps.objects.all()
    return render(request, 'form.html', context={"project": project, "area": area, "use": use})


