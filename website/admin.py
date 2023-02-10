from django.contrib import admin
from .models import  Picture
# Register your models here.



class PictureAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name' , ) }


admin.site.register(Picture , PictureAdmin)