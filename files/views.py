# framework imports
import mimetypes
import os
from datetime import date
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.shortcuts import render
from django.views.generic import View

# app/project imports
from common.utils.helpers import io_helpers, db_helpers
from files.forms import UploadFileForm
from files.models import File

class getFiles(View):
    user = User
    
    # GET uploads
    @login_required
    def get(self, request):
        group = db_helpers.get_organization_by_user_from_the_request(request)
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

    # GET files/downloads/{file_id}
    @login_required
    def get(self, request, file_id=-1):
        try:
            # TODO: download count do update, but it requires new page refresh. fix it.
            db_model = File.objects.get(id=file_id)        
            db_model.download_count =  db_model.download_count + 1
            db_model.save()

            filename = db_model.filepath.name.split('/')[-1]
            response = HttpResponse(db_model.filepath, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename

            return response
        except File.DoesNotExist:
            return HttpResponse(status=404)

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
        try:
            #title = request.FILES.charField(max_length=50)
            #form = UploadFileForm(request.POST, request.FILES)
            upload = request.FILES['myFile']
            io_helpers.save_file_to_disk(upload)

            """ if the code gets here, then it's safe to save the form into the database"""       
            group = db_helpers.get_organization_by_user_from_the_request(request)

            # TODO: Handle duplicate files
            file = File(
                group = group,
                user = request.user,
                name = upload.name,
                filepath = upload.name,
                uploaded = date.today(),
                download_count = 0
            )
            file.save()
        except:
            io_helpers.remove_uploaded_file(upload)
            return HttpResponse(status=500, content="Unable to save the file into the database.")

        # 200 would be OK with a normal REST API
        # I wouldn't use 201, because this endpoint also make database operation
        # but it's somehow needed to indicate in the client that the indeed succeed with uploading.
        # I guess redirect with some extra parameter is easiest.
        response = HttpResponse(status=302)
        
        # uploadFile.get - method
        # TODO: Show "Upload succeed" - message.
        # Maybe it could be using django messages, and middleware?
        response['Location'] = '?uploadResult=succeed'
        response['Method'] = 'GET'
        return response