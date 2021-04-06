import json
import os
import pyautogui
import time

from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcUvalueTmplForm
from .models import *

'''
import io as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
'''

# Create your views here.



def calcs(request):
    return render()


def uvalue_calcs(request):
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return render(request, 'uvalue_calc.html')

def uvalue_data(request):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uValueCalc.json')
    with open(json_path, 'r', encoding='UTF8') as f:
        json_file = json.load(f)
    return HttpResponse(json.dumps(json_file), content_type="application/json")

'''
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>')
'''


def uvalue_report(request):

    pyautogui.hotkey("ctrl", "p")
    time.sleep(120)

    '''
    return render_to_pdf(
        'uvalue_calc.html',
        {
            'pagesize': 'A4',
            'mylist': results,
        }
    )
    '''

    return HttpResponse(status=201)

def uvalue_save(request):
    if request.method == 'POST':    # POST 요청이면 폼 데이터를 처리한다
        form = CalcUvalueTmplForm(request.POST)
        if form.is_valid():
            tmpl = form.save(commit=False)
            tmpl.tmpl_save()
            return HttpResponse("저장되었습니다")
        else:
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=201)