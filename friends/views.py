from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def friends(request):
    return render (request,'friends/friends.html')