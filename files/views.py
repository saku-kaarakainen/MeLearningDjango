from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.models import User
from files.models import File
from files.forms import UploadFileForm
from datetime import date
from common.utils.db_helpers import get_organization_by_user_from_the_request

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views


class getFiles(View):
    user = User
    
    # GET uploads
    @login_required
    def get(self, request):
        group = get_organization_by_user_from_the_request(request)
        files = File.objects.filter(group_id=group.id).all()
        data = {
            'pagetitle': 'Uploaded files by the organization',
            'files': files,
        }
        return render(request, "listFiles.html", data)

class getFilesByUser(View):
    user = User
    
    # GET uploads/my
    @login_required
    def get(self, request):
        files = File.objects.filter(user_id=request.user.id).all()
        data = {
            'pagetitle': 'Uploaded files by the user',
            'files': files,
        }
        return render(request, "listFiles.html", data)

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
        #try:
        #title = request.FILES.charField(max_length=50)
        form = UploadFileForm(request.POST, request.FILES)

        #if not form.is_valid():
        #    return HttpResponseRedirect('upload/fail?reason=formIsNotValid')        

        """ if we get here, then it's safe to save the form into the database"""
        blob = request.FILES['myFile']            
        group = get_organization_by_user_from_the_request(request)

        file = File(
            group = group,
            user = request.user,
            blob = blob,
            uploaded = date.today(),
            download_count = 0
        )
        file.save()

        return HttpResponseRedirect('upload/success')
        
        # except:
        #     return HttpResponse(status=500, content="An error occured while uploading the file. If the error persists, bla bla bla.")

