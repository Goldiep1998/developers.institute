from django.shortcuts import render, redirect
from sell.models import Image
from sell.forms import ImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def error_404_view(request, exception):
    return render(request, '404.html')

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):

    all_images = Image.objects.filter(status='for-sale')

    return render(request, 'gallery.html', context={'images': all_images})

def image_info(request, id):
    image = Image.objects.get(id=id)
    return render(request, 'image_info.html', {'image': image})

@login_required()
def buy(request, id):
    image = Image.objects.get(id=id)
    image.status = 'sold'
    image.save()
    messages.success(request, f'You have purchased {image.title}')
    return redirect('gallery')

@login_required()
def delete(request, id):
    image = Image.objects.get(id=id)
    if request.user == image.seller:
        image.delete()
    else:
        raise Error("You do not have permission to access this data.")
    images = Image.objects.all()
    
    return render(request, 'gallery.html', {'images':images})

@login_required()
def edit(request, id):
    image = Image.objects.get(id=id)
    if request.user == image.seller:
        if request.method == 'POST':
            form = ImageForm(request.POST, instance=image)
            if form.is_valid():
                form.save()
                return redirect('gallery')

        else:
            form = ImageForm(instance=image)
            return render(request, 'edit_image.html', {'form': form})
    else:
        raise Error("You do not have permission to access this data.")
