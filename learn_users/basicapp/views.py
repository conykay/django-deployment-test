from django.shortcuts import render
from basicapp.userform import Userregform,Userproinf


from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basicapp.models import Userprofileinfo

def index(request):

    return render(request,'basicapp/index.html')

@login_required
def profile(request):

    userinfo = Userprofileinfo.objects.all()
    user_dict = {'userdict':userinfo}
    return render(request,'basicapp/profile.html',context = user_dict)

@login_required
def user_logout(request):
    logout(request)
    return render(request,'basicapp/login.html',{})

def register(request):
    register_form = Userregform()
    userinfo_form = Userproinf()

    registered = False

    if request.method == 'POST':

        register_form = Userregform(request.POST)
        userinfo_form = Userproinf(request.POST)

        if register_form.is_valid() and userinfo_form.is_valid():

            user = register_form.save()
            user.set_password(user.password)
            user.save()

            profile = userinfo_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.profile_pics =request.FILES['picture']
                profile.save()

                registered = True
        else:
            register_form = Userregform()
            userinfo_form = Userproinf()

    return render(request,'basicapp/register.html',{'register_form':register_form,'userinfo_form':userinfo_form,'registered':registered})

def user_login(request):

    if request.method=='POST':

        name = request.POST.get('surname')
        passw = request.POST.get('password')

        user = authenticate(username=name ,password=passw)

        if user:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('login failed for username:{}'.format(name))
            return HttpResponse('incorect login details')

    else:
        return render(request,'basicapp/login.html',{})
