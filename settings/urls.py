from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.settings,name='settings'),
    path('contact/',views.settings_cont,name='settings_cont'),
    path('password/',views.settings_pass,name='settings_pass'),
]