import datetime
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.shortcuts import render
# def catalog(request):
    # site_name = "Modern Musician"
    # response_html = u"<html><body>Welcome to %s.</body></html>" % site_name
    # return HttpResponse(response_html) 
# def catalog(request):
    # ren = render(request, 'sample.html', {'site_name': 'Modern Musician'})
    # return ren
# render là hàm có sẵn của django, nó sẽ trả về một HttpResponse
# httpresponse là một class của django, nó sẽ trả về một response
def catalog(request):
    site_name = "Modern Musician"
    c = {'site_name': site_name}
    t = loader.get_template('sample.html').render(c)
    response = HttpResponse(t)
    return response
# makemigrations: tạo ra các file migration
# migrate: chạy các file migration