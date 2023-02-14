from django.forms import ModelForm

from    django import forms
from .models import  User



class SignForm(ModelForm):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50 , required=False)
    last_name = forms.CharField(max_length=50 , required=False)
    email = forms.EmailField(required=False)



    class Meta:


        model = User
        fields = ['username' , 'password' , 'first_name', 'email' , 'last_name' , 'prof_pic']



class LoginForm(ModelForm):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


    class Meta :
        model = User
        fields = ['username' , 'password']








    #
    # name = forms.CharField(max_length=80 , label="name")
    # username = forms.CharField(max_length=30 , label="username" )
    # password = forms.CharField(max_length=30 ,label="password" )
    # phone = forms.CharField(max_length=15 , required=False , label='phon')
    # email = forms.EmailField(required=False , label='email')
    # prof_pic = forms.ImageField(required=False , label='prof_pic')