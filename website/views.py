from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from django.views.generic import ListView , TemplateView , CreateView
from .models import Picture
# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import CreatePictureForm
from django.utils.text import slugify
from utiles.cleanfiles import delete_file
from MySite.settings import BASE_DIR
# Create your views here.



def home(request):

    return render(request , 'website/index.html' )


@login_required()
def user_picture(request , username):

    real_user = (request.user.username)


    if real_user == username :

        user = get_object_or_404(User , username = username)
        pictures = user.pictures.all()

        paginator = Paginator(pictures,3)
        page_number = request.GET.get('p')
        page_obj = paginator.get_page(page_number)


        context = {
        'pictures' :pictures,
        'user' : user,
        'page_obj':page_obj,
        }


        return render(request , 'website/cli_pic.html' , context=context)

    else:

        return redirect(f'/pics/{real_user}')

def show_user_picture(request , username):

    user = get_object_or_404(User , username = username)
    pictures = user.pictures.all()

    paginator = Paginator(pictures, 3)
    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)

    context = {
        'pictures': pictures,
        'page_user': user,
        'page_obj': page_obj,
    }

    return render(request, 'website/user_pics.html', context=context)



def picture_detail(request , slug):

    picture = Picture.objects.get(slug = slug)

    user = picture.author
    context = {
        'picture' : picture,
        'pic_user' : user,

    }

    return render(request , 'website/picture_detail.html' , context=context)


@login_required()
def delete_pic (request , slug):

    picture = Picture.objects.get(slug = slug)
    user = picture.author
    url = str((str(BASE_DIR)) + picture.img.url)
    real_user = request.user

    if user == real_user:

        delete_file(url)
        picture.delete()

        return redirect(f'/pics/{user.username}')


    else:
        return redirect(f'/pics/{request.user.username}')



# class CreatePicture(LoginRequiredMixin,CreateView):
#     model = Picture
#
#     template_name = 'website/create.html'


@login_required()
def picture_create(request):

    user = request.user
    form = CreatePictureForm(request.POST , request.FILES)
    context = {
        "form": form
    }

    if request.method == "GET" :



        return render(request ,'website/create.html' ,context=context )

    if request.method =="POST":
        if form.is_valid():





            name = request.POST['name']
            img = request.FILES['img']
            slug = slugify(name+"-"+user.username)

            if  Picture.objects.filter(slug = slug).exists():

                error = 'A picture with the same name has already exist . Please Try Agine !'
                context = {
                        "form": form ,
                        "error" : error ,
                                }

                return render(request ,'website/create.html' ,context=context )



            else:


                user = request.user
                Picture.objects.create(author=user, name=name, img=img)
                return redirect(f'/pics/{request.user.username}')



        else:

            return render(request, 'website/create.html', context=context)






