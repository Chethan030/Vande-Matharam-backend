from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .permissions import *

class UserViews(ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UserSerial
    permission_classes=[IsAdmin]

class BgNameViews(ModelViewSet):
    queryset=Bgname.objects.all()
    serializer_class=BgNamesSerial
    permission_classes=[IsAdminOrReadOnly]

class BgimagesUploadView(ModelViewSet):
    queryset=BgImages.objects.all()
    serializer_class=BgimagesSerial
    permission_classes=[IsAdminOrReadOnly]

class NewsView(ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerial
    permission_classes=[IsAdminOrReadOnly]

class GurukulamActivityViews(ModelViewSet):
    queryset=GurukulamActivities.objects.all()
    serializer_class=GurukulamActSerial
    permission_classes=[IsAdminOrReadOnly]

class GurukulamGalleryViews(ModelViewSet):
    queryset=GurukulamGallery.objects.all()
    serializer_class=GurukulamGallerySerial
    permission_classes=[IsAdminOrReadOnly]

class AdrishyaGalleryViews(ModelViewSet):
    queryset=AdrishyaGalleryImages.objects.all()
    serializer_class=AdrishyaGallerySerial
    permission_classes=[IsAdminOrReadOnly]


class TeamViews(ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=TeamSerial
    permission_classes=[IsAdminOrReadOnly]


class SteeringBoardTeamViews(ModelViewSet):
    queryset=SteeringTeam.objects.all()
    serializer_class=SteeringBoardTeamSerial
    permission_classes=[IsAdminOrReadOnly]

class AdrishyaActView(ModelViewSet):
    queryset=AdrishtyActivities.objects.all()
    serializer_class=ActivitiesesAdrishyaSerial
    permission_classes=[IsAdminOrReadOnly]

class AdrishyaActimageViews(ModelViewSet):
    queryset=AdrishyaActImages.objects.all()
    serializer_class=AdrishyaActImagesSerial
    permission_classes=[IsAdminOrReadOnly]


