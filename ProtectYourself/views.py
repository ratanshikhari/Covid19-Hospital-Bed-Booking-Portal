from django.http import HttpResponse
from django.template import loader

def ProtectYourself(request):
    template = loader.get_template("ProtectYourself/About.html")
    return HttpResponse(template.render({}, request))

def ProtectYourselfAL(request):
    template = loader.get_template("ProtectYourself/AboutAL.html")
    return HttpResponse(template.render({}, request))
