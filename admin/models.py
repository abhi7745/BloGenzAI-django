from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Ads(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # Banner, Side_bar, Popup, Native, Video
    ad_type = models.CharField(max_length=50)
    # by_admin = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail_img = models.ImageField(upload_to='admin/ads/thumbnail_img')
    