from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.contrib.auth.decorators import login_required

@login_required()
def image_upload_view(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.seller = request.user
            new_form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})