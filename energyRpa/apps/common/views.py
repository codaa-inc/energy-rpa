import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import AuthUser
from apps.calculator.models import CalcUvalueTmpl
from django.contrib.auth import login, authenticate


def index(request) :
    return render(request, 'index.html')

def calcs(request):
    username = request.session.get('username')
    context = {"calc_list": CalcUvalueTmpl.objects.filter(username=username)}
    return render(request, 'list.html', context)

def signin(request) :
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