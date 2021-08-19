from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("salary",views.salary,name="About"),
    path("engineer",views.engineer,name="About")
]