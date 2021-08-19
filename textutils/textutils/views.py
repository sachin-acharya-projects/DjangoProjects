# Manual Documentations
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get("text","No strings given")
    removepuncInp = request.GET.get("removepunc","off")
    print(djtext)
    punc = "@!#$%^&*.,"
    analyzed = djtext
    for char in djtext:
        if char not in punc:
            analyzed = analyzed + char
    params = {'purpose':'Remove Punctuations',
              'anylyzed_text': analyzed
              }
    return render(request,'analyze.html',params)