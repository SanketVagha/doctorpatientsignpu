from django.shortcuts import render, redirect
from datetime import datetime
from docterpatientapp.models import User
from django.contrib import messages
from .form import FileUploadForm
from django.core.files.storage import default_storage
from django.conf import settings
import os
import hashlib
from django.http import JsonResponse


# Create your views here.
def index(request):
    user = User.objects.all()
    context = {
          'cont' : user
    }
    return render(request, 'signup.html', context)


def checkemailExists(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_exists = User.objects.filter(email=email).count()
        if user_exists == 0:
             return False        
        return True
    return False

def checkuserExists(request):
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username')
        user_exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': user_exists})
    return JsonResponse({'error': 'Invalid request'})

def profile(request,id):
    user = User.objects.filter(id = id).values()
    context = {
        'cont' : user
    }
    return render(request, 'profile.html', context)

def signup(request):
    if request.method == 'POST':
        data = {}
        existing_record = None
        if request.POST.get("fname"):
            data['fname'] = request.POST.get("fname")
            
        if request.POST.get("lname"):
            data['lname'] = request.POST.get("lname")
            
        if request.POST.get("email"):
            data['email'] = request.POST.get("email")
            
        nemail = User.objects.filter(email = data['email']).count()
        if nemail > 0:
            messages.success(request, "Email Already Exists!")
            context = {

            }
            return render(request, 'signup.html', context)

        if request.POST.get("username"):
            data['username'] = request.POST.get("username")
            
        nusername = User.objects.filter(username = data['username']).count()
        if nusername > 0:
            messages.success(request, "Username Already Exists!")
            context = {

            }
            return render(request, 'signup.html', context)

        if request.POST.get("userType"):
            data['userType'] = request.POST.get("userType")
            
        if request.POST.get("password"):
            data['password'] = hashlib.md5(request.POST.get("password").encode()).hexdigest()
            
        if request.POST.get("address"):
            data['address'] = request.POST.get("address")
            
        if request.POST.get("city"):
            data['city'] = request.POST.get("city")
            
        if request.POST.get("state"):
            data['state'] = request.POST.get("state")
            
        if request.POST.get("pincode"):
            data['pincode'] = request.POST.get("pincode")


        if len(request.FILES) != 0:
            uploaded_image = request.FILES.get('profile_image')
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            # Extract file extension from the original file name
            _, file_extension = os.path.splitext(uploaded_image.name)

            # Construct the new file name with the timestamp
            new_file_name = f"{timestamp}{file_extension}"
            # print(new_file_name)
            # Build the new file path
            new_file_path = os.path.join(f"{settings.MEDIA_ROOT}/upload", new_file_name)

            # Save the image with the new name
            default_storage.save(new_file_path, uploaded_image)

            data['profile_image'] = new_file_name
            request.FILES['profile_image'] = new_file_name
            form = FileUploadForm(data, request.FILES , instance=existing_record)
            if form.is_valid():
                form.save()
            user = User.objects.filter().create(**data)
            user.save()
            messages.success(request, "You Message has been sent!")
        # return render(request, 'profile.html', context)
        return redirect("profile",user.id)
    context = {

    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        if request.POST.get("email"):
            email = request.POST.get("email")
        if request.POST.get("password"):
            password = request.POST.get("password")
        
        user = list(User.objects.filter(email= email, password= hashlib.md5(password.encode()).hexdigest()).values())
        print(user)
        if not user:
            messages.success(request, "Invalid Email and Password!")
            return render(request, 'login.html')
        return redirect("profile", user[0]['id'])

    context = {
        
    }
    return render(request, 'login.html', context)