# files/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getFiles , name='index'),
    path('uploads', views.getFiles, name='uploads'),
    path('download', views.downloadFile, name='download'),
    path('upload', views.uploadFile, name='upload'),
]