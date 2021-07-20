from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import extendeduser

from .forms import CreateUserForm

def loginPage(request):
    context = {}
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['uname'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return HttpResponse("Logged IN!")
        else:
            return render(request, 'LoginPage/signinpage.html', {'error': "Invalid Login credentials "})
    else:
        return render(request, 'LoginPage/signinpage.html', context)


def registerPage(request):
    context = {}
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User .objects.get(username=request.POST['uname'])
                return render(request, 'LoginPage/signuppage.html', {'error': "Username has already been taken!"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                phnum = request.POST['phone_no']
                age = request.POST['age']
                email = request.POST['email']
                aadhar = request.POST['aadhar']
                state = request.POST['state']
                city = request.POST['city']
                newextendeduser = extendeduser(phone_no=phnum, age=age, email=email, aadhar=aadhar, state=state, city= city, user=user)
                auth.login(request, user)

                return HttpResponse("Registered!")
        else:
            return render(request, 'LoginPage/signuppage.html', {'error': "Password Dont match"})
    else:
        return render(request, 'LoginPage/signuppage.html', context)
