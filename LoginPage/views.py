from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from . models import extendeduser
from HospitalDetail.models import HospitalDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

def loginPage(request):
    context = {}
    if request.method == "POST":
        user = auth.authenticate(username=request.POST.get('uname'), password=request.POST.get('pass'))
        if user is not None:
            auth.login(request, user)
            return redirect('/userdetails/')
        else:
            return render(request, 'LoginPage/login.html', {'error': "Invalid Login credentials "})
    else:
        return render(request, 'LoginPage/login.html', context)

def logoutuser(request):
    logout(request)
    return render(request, 'HomePage/index.html', {})


def registerPage(request):
    context = {}
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST.get('uname'))
                return render(request, 'LoginPage/registrationform.html', {'error': "Username has already been taken!"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                phnum = request.POST['phone_no']
                name = request.POST['uname']
                age = request.POST['age']
                email = request.POST['email']
                aadhar = request.POST['aadhar']
                state = request.POST['state']
                city = request.POST['city']
                newextendeduser = extendeduser(phone_no=phnum, age=age, email=email, aadhar=aadhar, state=state, city= city, user=user, name=name)
                newextendeduser.save()
                auth.login(request, user)

                return redirect('/login/')
        else:
            return render(request, 'LoginPage/registrationform.html', {'error': "Password Dont match"})
    else:
        return render(request, 'LoginPage/registrationform.html', context)


@login_required(login_url='/login/')
def displayHDetails(request):
    print(request.POST)
    numbed = HospitalDetails.objects.all()
    for d in numbed:
        d.hBedAvail = d.hTotalNumBed - d.hBedBooked
        d.save()
    uDataNew = extendeduser.objects.get(user=request.user)
    if uDataNew.hBooked == True:
        if uDataNew.hBooked == True:
            return HttpResponse("Bed Already Booked!")
    else:
        if request.method == "POST":
            uDataNew.reportFile = request.FILES['reportFile']
            uDataNew.hSelectedName = request.POST['hName']
            uDataNew.hBooked = True
            uDataNew.save()
            hDetails = HospitalDetails.objects.get(hName=request.POST['hName'])
            hDetails.hBedBooked = hDetails.hBedBooked + 1
            hDetails.save()
    datas = HospitalDetails.objects.all()
    return render(request, 'LoginPage/beds.html', {'data': datas})


@login_required(login_url='/login/')
def userDetails(request):
    print(request.POST)
    uData = extendeduser.objects.filter(user=request.user)
    return render(request, 'LoginPage/details.html', {'udata': uData})


def viewHDetails(request):
    numbed = HospitalDetails.objects.all()
    for d in numbed:
        d.hBedAvail = d.hTotalNumBed - d.hBedBooked
        d.save()
    return render(request, 'LoginPage/bedsview.html', {'data': numbed})

