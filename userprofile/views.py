from django.shortcuts import redirect, render
from settings.models import userinfo
from .models import mypost
# Create your views here.
def userprofile(request):
    user = request.user
    return render (request,'userprofile/userprofile.html',{'user': user})
