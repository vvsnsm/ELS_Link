from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def settings(request):
    return render (request,'settings/settings.html')

def settings_cont(request):
    return render (request,'settings/settings-contact.html')

def settings_pass(request):
    return render (request,'settings/settings-password.html')