from django.urls import path
from website.views import home ,user_picture , show_user_picture , picture_detail , delete_pic , picture_create
app_name = 'website'

urlpatterns = [

    path('' , home , name= 'home'),
    path('pics/<slug:username>/' ,user_picture,  name='pics' ),
    path('pics/show/<slug:username>/' , show_user_picture , name = 'show_user_pics') ,
    path('pics/show/single/<slug:slug>/' ,picture_detail , name = 'single_pic' ),
    path('pics/delete/<slug:slug>/' ,  delete_pic  , name = 'pic_delete'),
    path('pic/create/' , picture_create , name = 'pic_create' ),





]