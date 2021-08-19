from django.urls import path
from .views import index
from .views import generateCode

urlpatterns = [
    path('', index, name="homePage"),
    path('generate', generateCode, name="code_generator")
]
