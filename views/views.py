from django.shortcuts import render, redirect
from classific.models import Image
from django.core.files.storage import FileSystemStorage
from classific.forms import ImageForm
from django.contrib.auth.decorators import login_required
from userflow.decorators import allowed_users,admin_only
# Create your views here.

@login_required(login_url='login')
def home_page(request):
    #только для текущего юзера
    #images= request.user.image_set.all()
    #для всех юзеров
    images=Image.objects.all().order_by('-id')

    context={
        'images':images,

    }

    return render(request,'index.html',context=context)


def viewimg(request,key):
    img=Image.objects.get(id=key)
    file_name=img.image.url.split('/')[-1]
    url= FileSystemStorage().url(img.image)
    context={
        'file_name':file_name,
        'img_url': url,
    }
    return render(request,'image.html',context=context)


@login_required(login_url='login')
@admin_only
def updateimg(request,id):
    image= Image.objects.get(id=id)
    form=ImageForm(instance=image)
    if request.method=='POST':
        form= ImageForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
    }
    return render(request,'form.html',context=context)


@login_required(login_url='login')
@admin_only
def deleteimg(request,id):
    image = Image.objects.get(id=id)
    image.delete()
    return redirect('/')


@login_required(login_url='login')
def run_inference(request,id):
    img = Image.objects.get(id=id)
    url = FileSystemStorage().url(img.image)
    from classific.inference import runInference
    prediction= runInference(url)
    context={
        'prediction':prediction,
        'imageurl':url,
    }
    return render(request,'upload.html',context=context)