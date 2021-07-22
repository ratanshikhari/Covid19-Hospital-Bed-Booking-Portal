from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import extendeduser
from HospitalDetail.models import HospitalDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .forms import CreateUserForm

def loginPage(request):
    context = {}
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['uname'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('/userdetails/')
        else:
            return render(request, 'LoginPage/signinpage.html', {'error': "Invalid Login credentials "})
    else:
        return render(request, 'LoginPage/signinpage.html', context)

def logoutuser(request):
    logout(request)
    return render(request, 'HomePage/index.html', {})


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
                name = request.POST['name']
                age = request.POST['age']
                email = request.POST['email']
                aadhar = request.POST['aadhar']
                state = request.POST['state']
                city = request.POST['city']
                newextendeduser = extendeduser(phone_no=phnum, age=age, email=email, aadhar=aadhar, state=state, city= city, user=user, name=name)
                newextendeduser.save()
                auth.login(request, user)

                return HttpResponse("Registered!")
        else:
            return render(request, 'LoginPage/signuppage.html', {'error': "Password Dont match"})
    else:
        return render(request, 'LoginPage/signuppage.html', context)

@login_required(login_url='/login/')
def displayHDetails(request):
    datas = HospitalDetails.objects.all()
    return render(request, 'LoginPage/beds.html', {'data': datas})

@login_required(login_url='/login/')
def userDetails(request):
    uData = extendeduser.objects.filter(user=request.user)
    return render(request, 'LoginPage/details.html', {'udata': uData})
