from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def HelpUs(request):
    template = loader.get_template("HelpUs/help.html")
    return HttpResponse(template.render({}, request))

def HelpUsAL(request):
    template = loader.get_template("HelpUs/helpAL.html")
    return HttpResponse(template.render({}, request))
