from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views
@login_required
def index(request):
    return HttpResponse("org page")

