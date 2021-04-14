import json as json_module
import os
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
from django.template import Context
from django.template.loader import get_template

def init_uvalue(request):
    return render(request, 'uvalue_calc.html')

def get_user_uvalue(request, uvalue_tmpl_cd):
    if uvalue_tmpl_cd is not None:
        return render(request, 'uvalue_calc.html', {"id": uvalue_tmpl_cd})

def select_uvalue(request, id):
    if id is not None:
        calc = CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=id)
        print(str(calc.query))
        json_serializer = json.Serializer()
        context = {"calc": json_serializer.serialize(calc)}
    return JsonResponse(context)

def insert_uvalue(request):
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

def update_uvalue(request, id):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save(update_fields=list(form.fields))
        return HttpResponseRedirect(self.get_success_url())

    if request.method == 'POST':    # POST 요청이면 폼 데이터를 처리한다
        form = CalcUvalueTmplForm(request.POST)
        if form.is_valid():
            #  delete and insert
            CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=id).delete()
            tmpl = form.save(commit=False)
            tmpl.uvalue_tmpl_cd = id
            tmpl.tmpl_save()
            context = {"result": True}
        else:
            context = {"result": False}
    else:
        context = {"result": False}
    return HttpResponse(json_module.dumps(context), content_type="application/json")

def load_data_uvalue(request):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uValueCalc.json')
    with open(json_path, 'r', encoding='UTF8') as f:
        json_file = json_module.load(f)
    return HttpResponse(json_module.dumps(json_file), content_type="application/json")

def report_uvalue(request, uvalue_tmpl_cd):
    calc = CalcUvalueTmpl.objects.filter(uvalue_tmpl_cd=uvalue_tmpl_cd).values()[0]
    print(str(calc.query))
    return render_to_pdf('uvalue_calc.html', {'pagesize': 'A4', 'mylist': calc})

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.decode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>')
