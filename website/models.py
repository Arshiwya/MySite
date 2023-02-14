from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
from django.utils.text import slugify

import datetime


# class User (models.Model):
#
#     name = models.CharField(max_length=50 , null=False)
#     username = models.CharField(max_length=50 , unique=True)
#     password = models.CharField(max_length=50 ,null=False)
#     email = models.EmailField(null=True)
#     phonnumber = models.BigIntegerField(null=True)
#     first_login = models.DateTimeField(auto_now=True)
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = "users"
#         ordering = ['-first_login']
#
#
#     def __str__(self):
#         return self.username








class Picture (models.Model):

    author = models.ForeignKey(User,null=True,blank=True ,on_delete=models.SET_NULL , related_name='pictures' )
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100  , unique=True)
    img = models.ImageField()
    created = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'
        ordering = ['created']


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+"-"+self.author.username)
        super(Picture, self).save(*args, **kwargs)



    def __str__(self):
        return self.name


