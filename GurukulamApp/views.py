from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class BgNameViews(ModelViewSet):
    queryset=Bgname.objects.all()
    serializer_class=BgNamesSerial

class BgimagesUploadView(ModelViewSet):
    queryset=BgImages.objects.all()
    serializer_class=BgimagesSerial

def home(request):
    return HttpResponse('hii')

