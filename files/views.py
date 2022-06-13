from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.models import User
from files.models import File
from files.forms import UploadFileForm
from datetime import date


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views


class getFiles(View):
    user = User

    # GET uploads?organizationId
    @login_required
    def get(self, request):
        return render(request, "listFiles.html")

class downloadFile(View):
    user = User

    # GET files/{file_id}
    @login_required
    def get(self, request):
        data = []
        return render(request, "downloadFile.html", data)

class uploadFile(View):
    user = User
    model = File

    # GET files/upload
    @login_required
    def get(self, request):
        return render(request, "uploadFile.html")


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
        # TODO: Support multiple organizations
        # 501: NotImplemented, because i follow these status codes: https://www.django-rest-framework.org/api-guide/status-codes/
        # This model assumes there is only one group per user
        if(request.user.groups.count() == 0):
            return HttpResponse(status=500, content="User is missing a group.")
        
        if(request.user.groups.count() > 1):
            return HttpResponse(status=501) # multi-group model is not supported
             
        #title = request.FILES.charField(max_length=50)
        form = UploadFileForm(request.POST, request.FILES)
    
        #if not form.is_valid():
        #    return HttpResponseRedirect('upload/fail?reason=formIsNotValid')        

        """ if we get here, then it's safe to save the form into the database"""
        blob = request.FILES['myFile']
        
        orgs = request.user.groups.all()
        org = orgs[0]

        if(org is None):
            return HttpResponse(status=500, content="Unexpected none")


        file = File(
            organization = org,
            blob = blob,
            uploaded = date.today(),
            download_count = 0
        )
        file.save()

        return HttpResponseRedirect('upload/success')

