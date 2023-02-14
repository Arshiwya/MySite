from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):

    prof_pic = models.ImageField(null=True ,upload_to="profpics/" , blank=True ,default='profpics/defult.jpg')
    special_til=models.DateTimeField(null=True , default=timezone.now)

    def is_special(self):

        if self.special_til > timezone.now():

            return True

        else:

            return False

