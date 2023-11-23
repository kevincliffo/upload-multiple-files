import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import UploadedFile, ExtraUploadedFile
from .forms import UploadFileForm

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def upload_and_display_files(request):
    files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            counter = 1
            parent_file = None
            for uploaded_file in request.FILES.getlist('files'):
                if counter == 1:
                    counter = counter + 1
                    parent_file = UploadedFile.objects.create(file=uploaded_file)
                else:
                    ExtraUploadedFile.objects.create(uploaded_file=parent_file, file=uploaded_file)

            return redirect('app:upload-and-display')
    else:
        form = UploadFileForm()

    return render(request, 'app/index.html', {'form': form, 'files': files})