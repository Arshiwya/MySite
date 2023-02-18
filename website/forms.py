from django.forms import ModelForm

from   django import forms
from accounts.models import User
from .models import Picture
from django.forms.widgets import FileInput

class CreatePictureForm(ModelForm):

    class Meta :
        model = Picture
        fields = ['name' , 'img']


class EditProfileForm(ModelForm):
    prof_pic = forms.ImageField(widget=FileInput)

    class Meta :
        model = User
        fields = ['first_name' ,'last_name','email','prof_pic' ]
