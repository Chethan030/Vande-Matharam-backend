
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
router=DefaultRouter()

router.register(r'users',UserViews)
router.register(r'home/act',HomeActViews)
router.register(r'news',NewsView)
router.register(r'gukulam_activities',GurukulamActivityViews)
router.register(r'gallery/gurukulam',GurukulamGalleryViews)
router.register(r'gallery/adrishya',AdrishyaGalleryViews)
router.register(r'team',TeamViews)
router.register(r'team/steeringboard-team',SteeringBoardTeamViews)
router.register(r'adrishya/activities',AdrishyaActView)
router.register(r'adrishya/image',AdrishyaActimageViews)



urlpatterns=[
    path('token/',TokenObtainPairView.as_view())
]+router.urls
