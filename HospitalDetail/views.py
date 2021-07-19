from django.http import HttpResponse

def HospitalDetails(request):
    return HttpResponse('<H2>Details of Hospitals</h2>')
