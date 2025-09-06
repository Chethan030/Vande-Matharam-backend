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

class NewsView(ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerial

class GurukulamActivityViews(ModelViewSet):
    queryset=GurukulamActivities.objects.all()
    serializer_class=GurukulamActSerial

class GurukulamGalleryViews(ModelViewSet):
    queryset=GurukulamGallery.objects.all()
    serializer_class=GurukulamGallerySerial

class AdrishyaGalleryViews(ModelViewSet):
    queryset=AdrishyaGalleryImages.objects.all()
    serializer_class=AdrishyaGallerySerial


class TeamViews(ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=TeamSerial


class SteeringBoardTeamViews(ModelViewSet):
    queryset=SteeringTeam.objects.all()
    serializer_class=SteeringBoardTeamSerial

class AdrishyaActView(ModelViewSet):
    queryset=AdrishtyActivities.objects.all()
    serializer_class=ActivitiesesAdrishyaSerial

class AdrishyaActimageViews(ModelViewSet):
    queryset=AdrishyaActImages.objects.all()
    serializer_class=AdrishyaActImagesSerial


