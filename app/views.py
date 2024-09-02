from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def home(request) :
    return  render(request,"home.html")


def view_all_flights(request):
    flwo=Flights.objects.all()
    d={'flwo':flwo}
    if d:
        return render(request,'display.html',d)
    else:
        return HttpResponse('no Flights are avalable')
def Add_flights(request):
    EFDO=homepageform()
    d={'EFDO':EFDO}
    if request.method=='POST':
        FFDO=homepageform(request.POST)
        if FFDO.is_valid():
            FFDO.save()
            return HttpResponse('added flight successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'add_flights.html',d)