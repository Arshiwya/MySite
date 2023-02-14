from django.shortcuts import render , HttpResponse ,redirect
from .forms import SignForm , LoginForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.views import LoginView


from django.shortcuts import resolve_url
def sign_user(request):
    form = SignForm(request.POST , request.FILES)

    if request.method =='POST':


        if form.is_valid():
            if request.FILES:
                username = request.POST["username"]
                password = request.POST["password"]
                if request.POST["last_name"]:

                    last_name = request.POST["last_name"]

                else:

                    last_name = ''

                if request.POST["first_name"]:

                    first_name = request.POST["first_name"]

                else:

                    first_name = ''
                if request.POST["email"]:

                    email = request.POST["email"]



                else:
                    email = ''

                if request.FILES["prof_pic"]:

                    prof_pic = request.FILES["prof_pic"]
                else:
                    prof_pic = 'profpics/defult.jpg'

                user = User.objects.create_user(username=username,
                                                password=password,
                                                last_name=last_name,
                                                first_name=first_name,
                                                email=email,
                                                prof_pic=prof_pic)

                login(request, user)

                return redirect(f'/pics/{username}')

            else:
                username = request.POST["username"]
                password = request.POST["password"]
                if request.POST["last_name"]:

                    last_name = request.POST["last_name"]

                else:

                    last_name = ''

                if request.POST["first_name"]:

                    first_name = request.POST["first_name"]

                else:

                    first_name = ''
                if request.POST["email"]:

                    email = request.POST["email"]



                else:
                    email = ''

                user = User.objects.create_user(username=username,
                                                password=password,
                                                last_name=last_name,
                                                first_name=first_name,
                                                email=email
                                                )

                login(request, user)

                return redirect(f'/pics/{username}')







        else:
            error = 'This Username Has Already Take. Try Again!!!'

            return render(request, template_name='accounts/sign.html', context={"form": SignForm , "error" :error})

    else:
        return render(request , template_name='accounts/sign.html' ,context= {"form" : SignForm})



    return render(request , template_name='accounts/sign.html' ,context= {"form" : SignForm})


def logout_user(request):
    logout(request)
    messages.success(request , "logged out successfuly !")

    return redirect('website:home')






# def login_user(request):
#
#     form = LoginForm(request.POST , request.FILES)
#
#
#
#     if request.method == "POST":
#         print("xxxxxxxxxxxx")
#
#         if form.is_valid():
#
#
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#
#                 login(request , user)
#
#
#                 return redirect(f'/pics/{username}')
#
#
#             else:
#
#                 return render(request, 'registration/login.html' , context={"form": LoginForm})
#
#
#         else:
#             print(form)
#             return render(request, template_name='registration/login.html', context={"form": LoginForm})
#
#     else:
#         print("yyyyyyyyyyyyy")
#         return render(request , template_name='registration/login.html' ,context= {"form" : LoginForm})



class LoginviewMe(LoginView):
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(f'/pics/{self.request.user.username}')