from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.core.files.storage import FileSystemStorage

# Create your views here.

def form (request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.user=request.user
            form.save()
            return redirect('home')

    context = {
        'form': ImageForm(),
    }
    return render(request,'form.html',context=context)







