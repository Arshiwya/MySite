from django.contrib import admin
from .models import User , Picture
# Register your models here.

admin.site.register(User)

class PictureAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name' , ) }


admin.site.register(Picture , PictureAdmin)