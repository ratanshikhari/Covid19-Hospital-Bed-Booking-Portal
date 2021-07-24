from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def HomePage(request):
    template = loader.get_template("HomePage/index.html")
    return HttpResponse(template.render({}, request))

def HomePageAL(request):
    template = loader.get_template("HomePage/indexAL.html")
    return HttpResponse(template.render({}, request))
