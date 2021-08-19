from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
import os

# Create your views here.
def index(request):
    params = {
        'alert': 'SACHIN ACHARYA QR_CODE GENERATOR',
        'download': ''
    }
    return render(request, 'apps/index.html', params)



def generateCode(request):
    data = str(request.GET.get("input", ""))
    output_file_name = str(request.GET.get("name", ""))
    output_file_name = output_file_name.replace(" ", "_")
    output_path = os.path.join('.\\qr_code_app\\static', 'Output')
    qrcode = pyqrcode.create(data)
    qrcode.png(f"{output_path}\\{output_file_name}.png", scale=8)
    params = {
        'download': f'Output\\{output_file_name}.png',
        'alert': 'Successfully Generated Code'  
    }

    return render(request, 'apps/index.html', params)