from collections.abc import Iterable
from django.db import models

from accounts.models import User
# from django.contrib.auth.models import AbstractUser
# for importing auth_user table
# from django.contrib.auth.models import User

# slugify for corresponding title name of blog
from django.utils.text import slugify
import random, string


class Blog_category(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name
    

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(Blog_category, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(blank=True, max_length=225)
    title = models.CharField(max_length=1024)
    thumbnail_img = models.ImageField(upload_to='blog/thumbnail_img')
    content = models.TextField()
    ban = models.BooleanField(default=False)
    by_admin = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # avoiding duplicates entries titles
        if not self.pk and Blog.objects.filter(id=self.pk).exists() or (self.pk and Blog.objects.filter(title=self.title).exists()):
            # If this is a new object and a title with the name already exists
            # add a random string to the title
            random_string = ''.join(random.choices(string.ascii_lowercase, k=5))

            # self.title = f"{self.title}-{random_string}"
            title = f"{self.title}-{random_string}"
            self.slug = slugify(title)[:225]
            # print('database if call################################################################', self.pk, Blog.objects.filter(title=self.title).count(), args, kwargs)

        else:
            self.slug = slugify(self.title)[:225]
            # print('database else call################################################################', self.pk, Blog.objects.filter(title=self.title).count(), args, kwargs)

        super(Blog, self).save(*args, **kwargs)


    def __str__(self):
        return self.slug
    

class Blog_tag(models.Model):
    blog_category = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.CharField(max_length=225)

    def __str__(self):
        return self.tag


class Like(models.Model):
    blog=models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key=True)
    likes = models.BigIntegerField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

class Subscriber(models.Model):
    creator_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='creator_id')
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber_id')
    subscribers = models.BigIntegerField()