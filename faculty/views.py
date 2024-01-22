from django.shortcuts import render
from .models import *
from django.http import HttpResponse,Http404
from django.conf import settings
from django.conf.urls.static import static
from Student_app.models import *
# Create your views here.

def home(request):
    return HttpResponse('hello')
