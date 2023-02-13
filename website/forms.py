from django.forms import ModelForm

from   django import forms

from .models import Picture


class CreatePictureForm(ModelForm):

    class Meta :
        model = Picture
        fields = ['name' , 'img']



