from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def groups(request):
    return render (request,'groups/groups.html')