from django.shortcuts import render,redirect
from .forms import CreateUserForm,UpdateProfileForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unuthenticated_user,allowed_users

from .models import Profile
from classific.models import Image
# Create your views here.


@allowed_users(allowed_roles=['user'])
def update_profile(request):
    if request.method == 'POST':
        form1=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form1.is_valid():
            form1.save()
        form2=UpdateUserForm(request.POST,instance=request.user)
        if form2.is_valid():
            form2.save()
        return redirect('user')
    form= UpdateProfileForm(instance=request.user.profile)
    form2= UpdateUserForm(instance=request.user)

    context={
        'userform':form2,
        'form':form,
    }
    return render(request,'update_user.html',context=context)


def user_page(request):
    images= request.user.image_set.all()

    context = {
        'images': images,

    }
    return render(request,'user.html',context=context)


@unuthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()


            messages.success(request,'Account was create for ' + form.cleaned_data.get('username'))
            return redirect('login')


    context={
        'form':form
    }
    return render(request,'register.html',context=context)

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group


#@receiver(post_save,sender=User)
def created_profile(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)
        Profile.objects.create(user=instance)

post_save.connect(created_profile,sender=User)




@unuthenticated_user
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is uncorrect!')
    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')