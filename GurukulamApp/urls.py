
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'bg_name',BgNameViews)
router.register(r'bg_images',BgimagesUploadView)
router.register(r'news',NewsView)
router.register(r'gukulam_activities',GurukulamActivityViews)
router.register(r'gallery/gurukulam',GurukulamGalleryViews)

urlpatterns=router.urls
