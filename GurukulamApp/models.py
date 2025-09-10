from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='staff'):
        if not email:
            raise ValueError("Users must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password, role='admin')

class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (('admin', 'Admin'),('staff','Staff'))
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def _str_(self):
        return f"{self.email} ({self.role})"
    
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
    
class HomepageActivites(models.Model):
    tittle=models.CharField(max_length=70)
    des=models.TextField()
    image=models.ImageField(upload_to='activites_image')

    def __str__(self):
        return self.tittle