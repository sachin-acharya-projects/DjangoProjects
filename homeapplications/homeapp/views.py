from django.shortcuts import render
from .models import Person

def index(request):
    person = Person.objects.all()
    params = { 'data': person }
    return render(request, 'homeapp/index.html', params)