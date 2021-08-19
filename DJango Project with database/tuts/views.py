from django.shortcuts import render
from .models import Engineers
from math import ceil
# Create your views here.

def index(request, engineers=None):
    engineer = Engineers.objects.all()
    print(engineer)
    n = len(engineer)
    slideNo = n//4 + ceil((n/4) - (n//4))
    params = {
        'engineer': engineer,
        'slideAmt': slideNo,
        'range': range(slideNo)
    }
    return render(request,"tuts/index.html",params)

def salary(request):
    return render(request,"tuts/salary.html")

def engineer(request):
    return render(request,"tuts/engineer.html")