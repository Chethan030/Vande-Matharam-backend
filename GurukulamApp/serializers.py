from rest_framework import serializers
from .models import *

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['id','email','password','role']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        password=validated_data.pop('password')
        user=Users(**validated_data)
        user.set_password(password)
        user.save()
        return user
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

class GurukulamActSerial(serializers.ModelSerializer):
    class Meta:
        model=GurukulamActivities
        fields='__all__'

class AdrishyaGallerySerial(serializers.ModelSerializer):
    class Meta:
        model=AdrishyaGalleryImages
        fields=['id','image','date']
    
class GurukulamGallerySerial(serializers.ModelSerializer):
    class Meta:
        model=GurukulamGallery
        fields=['id','date','images']

class SteeringBoardTeamSerial(serializers.ModelSerializer):
    class Meta:
        model=SteeringTeam
        fields='__all__'
        
class TeamSerial(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'

class AdrishyaActImagesSerial(serializers.ModelSerializer):
    class Meta:
        model=AdrishyaActImages
        fields=['adrishya','images']

class ActivitiesesAdrishyaSerial(serializers.ModelSerializer):
    image=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=AdrishtyActivities
        fields=['id','title','des','image']
    
    def get_image(self,obj):
        if obj.adrishyaactivities_images:
            serializers_data=AdrishyaActImagesSerial(obj.adrishyaactivities_images.all(),many=True,context=self.context).data
            images=[item['images'] for item in serializers_data]
            return images
        return 'no'




