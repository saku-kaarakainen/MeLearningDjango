from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views

# GET uploads?organizationId
@login_required
def getFiles(request):
    return render(request, "files/listFiles.html")

# GET files/{file_id}
@login_required
def downloadFile(request):
    data = []
    return render(request, "files/downloadFile.html", data)


# POST files/upload, returns 201
@login_required
def uploadFile(request):
    return render(request, "files/uploadFile.html")

