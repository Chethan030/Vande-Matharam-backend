

from rest_framework import serializers
from .models import *

class BgNamesSerial(serializers.ModelSerializer):
    class Meta:
        model=Bgname
        fields='__all__'

class BgimagesSerial(serializers.ModelSerializer):
    class Meta:
        model=BgImages
        fields='__all__'
        
        
class NewsSerial(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'
    

        
