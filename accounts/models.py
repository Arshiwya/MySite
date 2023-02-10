from django.db import models




class User (models.Model):

    name = models.CharField(max_length=80 , null=False)
    username = models.CharField(max_length=30 , unique=True)
    password = models.CharField(max_length=30 , null=False)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    prof_pic = models.ImageField(upload_to='prof_pics/' , null=True)
    sign_up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural ='Users'


    def __str__(self):
        return (self.username)
