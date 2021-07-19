from django.http import HttpResponse

def login(request):
    return HttpResponse("<h1>Please fill your login details</h1>")
