from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import creategroup

def groups(request):
    if request.method == 'POST':
        name=request.POST['name']
        description=request.POST['description']
        image=request.POST['image']

        creategroupdata=creategroup(title=name,description=description,image=image)
        creategroupdata.save()
    result = creategroup.objects.all()
    dicti = { 'result' : result }
    return render(request,'groups/groups.html',dicti)

    