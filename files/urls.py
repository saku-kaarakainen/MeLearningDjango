# files/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getFiles.as_view(), name='index'),
    path('uploads', views.getFiles.as_view(), name='uploads'),
    path('my', views.getFilesByUser.as_view(), name='my_uploads'),
    path('downloads/<int:file_id>', views.downloadFile.as_view(), name='downloads'),
    path('upload', views.uploadFile.as_view(), name='upload'),
]