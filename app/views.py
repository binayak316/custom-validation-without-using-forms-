from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Userlog
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            context = {
                    'name' : name, 
                    'email': email,
                }
            if not email or not name or not password1 or not password2:
                
                if not name:
                    messages.error(request,'Name is required')
                    return render(request, 'app/register.html', context)
                elif not email:
                    messages.error(request,'Email is required')
                    return render(request, 'app/register.html', context)
                elif not password1:
                    messages.error(request,'Password is required')
                    return render(request, 'app/register.html', context )
                elif not password2:
                    messages.error(request,'Repeat the same password')
                    return render(request, 'app/register.html', context )
            elif(password1 != password2):
                messages.error(request,"Password didn't match")
                return render(request, 'app/register.html', context)

            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email is already exists')
                return render(request, 'app/register.html', context)

            elif(password1 == password2):
                if len(password1)>=9:
                    if not any(char.isdigit() for char in password1):
                        messages.error(request,"Password needs any digit")
                        return render(request, 'app/register.html', context )
                    elif not any(char.isupper() for char in password1):
                        messages.error(request,"Password needs any uppercase letter")
                        return render(request, 'app/register.html', context )
                    elif not any(char.islower()for char in  password1):
                        messages.error(request,"Password needs any lowercase letter")
                        return render(request, 'app/register.html', context )  
                    elif not any(char.isalnum()for char in password1):
                        messages.error(request,"Password should contain special characters")
                        return render(request, 'app/register.html', context )
                else:
                    messages.error(request,"Password must contain at least 9 characters")
                    return render(request, 'app/register.html', context)
                new_user = User.objects.create_user(username=name, email=email, password=password1)
                new_user.save()
                # print(name,email,password1,password2)
                messages.success(request,"User created successfully")
                return redirect('login')

        else:
            return render(request,'app/register.html')
    else:
        return redirect('/')
        

def login_user(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            username = request.POST.get('name')
            password = request.POST.get('password')
            if username and password:
                users = authenticate(username=username, password=password)
                if users is not None:
                    login(request, users)
                    return redirect('index')
                else:
                    messages.error(request,"username and password is not correct")
            else:
                messages.error(request, "Please fill the fields")
        return render(request, 'app/login.html')
    else:
        return HttpResponseRedirect('/')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):

    return render(request, 'app/index.html')

# def user_task(request, name, ipaddress, task):
#     name = Userlog.objects.get(name=name)
#     ipaddress = Userlog.objects.get(ipaddress=ipaddress)
#     task = Userlog.objects.get(task=task)

#     context = {
#         name:'name',
#         ipaddress :'ipaddress',
#         task: 'task',
#     }

#     return render(request, 'app/index.html', context)