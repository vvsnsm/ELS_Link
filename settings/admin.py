from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import userinfo
class userform(ImportExportMixin,admin.ModelAdmin):
    list_display = ['fname','lname','username']

admin.site.register(userinfo,userform)