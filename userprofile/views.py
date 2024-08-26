from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userprofile(request):
    return render (request,'userprofile/userprofile.html')
