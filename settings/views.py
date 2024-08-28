from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . models import userinfo

def settings(request):
    if request.method == 'POST':
        fname1 = request.POST['first_name']
        lname1 = request.POST['last_name']
        username1 = request.POST['username']
        userdetailsdata = userinfo(fname=fname1,lname=lname1,username=username1)
        userdetailsdata.save() 
    return render (request,'settings/settings.html')

def settings_cont(request):
    return render (request,'settings/settings-contact.html')

def settings_pass(request):
    return render (request,'settings/settings-password.html')