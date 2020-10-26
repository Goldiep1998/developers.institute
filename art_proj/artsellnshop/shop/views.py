from django.shortcuts import render, redirect
from sell.models import Image
from sell.forms import ImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


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
    order = order_number()
    email_buyer(request, order)
    email_seller(request, image)
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

def order_number():
    order_list = {}
    number = randint(0,999999999)
    while number in order_list:
        number = randint(0,999999999)
    order_list.update({number: number})
    return number
        
def email_buyer(request, order):
    subject = f'Your Order #{order}'
    message = f'Thank you for purchasing at ArtSellNShop. Your order number is {order}.'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [request.user.email,]
    send_mail( subject, message, email_from, recipient_list) 
    return

def email_seller(request, image):
    seller = User.objects.get(id = image.seller.id)
    subject = f'Your Artwork has been sold!'
    message = f'Thank you for using ArtSellNShop. Your artwork {image.title} has been purchased by {request.user}. Buyers contact email is {request.user.email}'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [seller.email,]
    send_mail( subject, message, email_from, recipient_list) 
    return
