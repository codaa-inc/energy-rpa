import json as json_module
import os
import pyautogui
import time
import io as StringIO

from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import CalcUvalueTmplForm
from .models import CalcUvalueTmpl
from django.core.serializers import json
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django_xhtml2pdf.utils import generate_pdf


def uvalue_init(request):
    return render(request, 'uvalue_calc.html')

def uvalue_user(request, uvalue_tmpl_cd):
    if uvalue_tmpl_cd is not None:
        return render(request, 'uvalue_calc.html', {"id": uvalue_tmpl_cd})


def uvalue_select(request, id):
    if id is not None:
        calc = CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=id)
        json_serializer = json.Serializer()
        context = {"calc": json_serializer.serialize(calc)}
    return JsonResponse(context)


def uvalue_insert(request):
    if request.method == 'POST':    # POST 요청이면 폼 데이터를 처리한다
        form = CalcUvalueTmplForm(request.POST)
        if form.is_valid():
            tmpl = form.save(commit=False)
            tmpl.tmpl_save()
            context = {"result": True}
        else:
            context = {"result": False}
    else:
        context = {"result": False}
    return HttpResponse(json_module.dumps(context), content_type="application/json")

def uvalue_update(request, id):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save(update_fields=list(form.fields))
        return HttpResponseRedirect(self.get_success_url())

    if request.method == 'POST':    # POST 요청이면 폼 데이터를 처리한다
        form = CalcUvalueTmplForm(request.POST)
        if form.form_valid():
            #  TODO - selected row update
            calc = CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=id)
            calc = form
            calc.save()
            context = {"result": True}
        else:
            context = {"result": False}
    else:
        context = {"result": False}
    return HttpResponse(json_module.dumps(context), content_type="application/json")



def uvalue_data(request):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uValueCalc.json')
    with open(json_path, 'r', encoding='UTF8') as f:
        json_file = json_module.load(f)
    return HttpResponse(json_module.dumps(json_file), content_type="application/json")


def uvalue_report(request):
    calc = CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=3)
    result = generate_pdf('uvalue_calc.html', file_object=HttpResponse(content_type='application/pdf'), context={'calc':calc})
    return result

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>')
