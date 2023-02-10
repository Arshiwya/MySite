from django.shortcuts import render
from django.views.generic import ListView , TemplateView
from .models import Picture
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.



# def home(request):
#
#     return render(request , 'website/index.html' )
#

class Home (TemplateView):
    template_name = 'website/index.html'


# def login(request):
#
#     return render(request , 'website/sign.html')




class MyPicture (LoginRequiredMixin,ListView):

    LOGIN_REDIRECT_URL = 'website:pics'



    model = Picture
    template_name = 'website/pictures.html'
    paginate_by = 3





