from django.db import models


from django.contrib.auth.models import AbstractUser
# for importing auth_user table
# from django.contrib.auth.models import User



# Create your models here.
class User(AbstractUser):
    role=models.CharField(max_length=50,null=True,blank=True)
    ban = models.BooleanField(default=False)
    premium_member = models.BooleanField(default=False)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail_img = models.ImageField(upload_to='blog/thumbnail_img')
    content = models.TextField()
    ban = models.BooleanField(default=False)
    by_admin = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    blog=models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key=True)
    likes = models.BigIntegerField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

class Subscriber(models.Model):
    creator_id = models.ForeignKey(User,on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribers = models.BigIntegerField()