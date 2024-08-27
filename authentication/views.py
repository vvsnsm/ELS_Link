from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Email or Password Invalid!')

    return render(request,'authentication/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully !')
    return redirect('login')

def authregistration(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        # phno = request.POST['phno']
        # dob = request.POST['dob']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist')
            # elif User.objects.filter(phno=phno).exists():
            #     messages.error(request, 'Account already exit with this Ph No.')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('userprofile')

        else:
            messages.error(request, 'Password and Confirm Password Not Matched')

    return render(request,'authentication/registration.html')

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['username']
        if User.objects.filter(email=email).exists():
            return redirect('userprofile')
        else:
            messages.error(request, 'Account not found with the email.')
    return render(request,'authentication/forget.html')
