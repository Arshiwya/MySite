from django.shortcuts import render , HttpResponse ,redirect
from .forms import SignForm
from django.contrib.auth import logout
from django.contrib import messages



def sign_user(request):
    form = SignForm(request.POST , request.FILES)
    print(request.method)
    if request.method =='POST':


        if form.is_valid():
            form.save()

            return redirect('website:home')

        else:
            return render(request, template_name='accounts/sign.html', context={"form": SignForm})

    else:
        return render(request , template_name='accounts/sign.html' ,context= {"form" : SignForm})



    return render(request , template_name='accounts/sign.html' ,context= {"form" : SignForm})







def logout_user(request):
    logout(request)
    messages.success(request , "logged out successfuly !")

    return redirect('website:home')

