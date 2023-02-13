from django.contrib import admin
from .models import  Picture
# Register your models here.



class PictureAdmin (admin.ModelAdmin):
    list_display = ['author' , 'name' , 'slug' , 'created']
    prepopulated_fields = {'slug' : ('name' , ) }


admin.site.register(Picture , PictureAdmin)