from django.db import models

class Bgname(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class BgImages(models.Model):
    bgname=models.OneToOneField(Bgname,on_delete=models.CASCADE,related_name='bg_images_for_each')
    image=models.ImageField(upload_to='bg-images')

    def __str__(self):
        return self.bgname.name

class News(models.Model):
    news_name=models.CharField(max_length=60)
    image=models.ImageField(upload_to='news_images')
    description=models.TextField()
    date=models.DateField(auto_created=False)

    def __str__(self):
        return self.news_name

class GurukulamActivities(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='gurukulam_activities')
    des=models.TextField()

    def __str__(self):
        return self.title
    
class GurukulamGallery(models.Model):
    images=models.ImageField(upload_to="images_gurukulam_gallery")
    date=models.DateField(auto_created=False)
    

class AdrishyaGalleryImages(models.Model):
    image=models.ImageField(upload_to='AdrishyaGallery')
    date=models.DateField(auto_now_add=False)

class Team(models.Model):
    name=models.CharField(max_length=80)
    designation=models.TextField()
    des=models.TextField()
    image=models.ImageField(upload_to='team_images')
    
    def __str__(self):
        return self.name


class SteeringTeam(models.Model):
    name=models.CharField(max_length=70)
    image=models.ImageField(upload_to='steeringBoardTeam')

    def __str__(self):
        return self.name

class AdrishtyActivities(models.Model):
    title=models.CharField(max_length=60)
    des=models.TextField()


    def __str__(self):
        return self.title
    
class AdrishyaActImages(models.Model):
    adrishya=models.ForeignKey(AdrishtyActivities,on_delete=models.CASCADE,related_name='adrishyaactivities_images')
    images=models.ImageField(upload_to='adrishya/activities')
    
    def __str__(self):
        return  self.adrishya.title