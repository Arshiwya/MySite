from django.urls import path
from website.views import Home ,MyPicture

app_name = 'website'

urlpatterns = [

    path('' , Home.as_view() , name= 'home'),
    path('pics/' ,MyPicture.as_view() , name='pics' ),


]