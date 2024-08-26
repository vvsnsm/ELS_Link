from django.contrib import admin

# Register your models here.
from .models import newsmodel
admin.site.register(newsmodel)