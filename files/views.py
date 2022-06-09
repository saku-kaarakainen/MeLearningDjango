from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.models import User
from files.models import File

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views


class getFiles(View):
    user = User

    # GET uploads?organizationId
    @login_required
    def get(self, request):
        return render(request, "files/listFiles.html")

class downloadFile(View):
    user = User

    # GET files/{file_id}
    @login_required
    def get(self, request):
        data = []
        return render(request, "files/downloadFile.html", data)

class uploadFile(View):
    user = User
    model = File

    # GET files/upload
    @login_required
    def get(self, request):
        return render(request, "files/uploadFile.html")


    """
        Route: POST files/upload

        Request and Response objects: 
        https://docs.djangoproject.com/en/4.0/ref/request-response/
            Files:  A dictionary-like object containing all uploaded files.
                    Each key in FILES is the name from the <input type="file" name="">.
                    Each value in FILES is an UploadedFile.
    """
    @login_required
    def post(self, request):
        #title = request.FILES.charField(max_length=50)
        # file = File(request.FILES.myBlob)

        # if file.is_valid():
        #     file.save()
        #     return HttpResponseRedirect('upload/success')
        
        return HttpResponseRedirect('upload/fail')
