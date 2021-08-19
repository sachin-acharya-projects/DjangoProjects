from django.urls import path
from .import views
from django.conf import settings # Use for media
from django.conf.urls.static import static # Use for media
urlpatterns = [
    path('', views.index, name='index')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # For media
