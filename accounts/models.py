# This Django app is build for automation using python, build by Abhijith KR 

from django.db import models

# import for custom user model - fields
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Usage: creating a model class, add this in settings AUTH_USER_MODEL = 'app_name.model_class_name', register in admin.py 
class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Recruiter'),
    )

    role=models.CharField(max_length=50,null=True,blank=True, choices=ROLE_CHOICES)
    ban = models.BooleanField(default=False)
    premium_member = models.BooleanField(default=False)

class User_Account(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.email
    