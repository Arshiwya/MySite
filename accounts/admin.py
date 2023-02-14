from django.contrib import admin
#from django.contrib.auth.models import User
from   .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin (UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']+=('prof_pic',)
    UserAdmin.fieldsets[3][1]['fields'] += ('special_til',)



admin.site.register(User  , CustomUserAdmin)