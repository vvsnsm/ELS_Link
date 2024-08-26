from django.shortcuts import render
from django.http import HttpResponse
from .models import newsmodel

def index(request):
    newsdata = newsmodel.objects.get(id=1)
    context = {
        'newsdata' : newsdata
    }
    return render (request,'index.html',context)