from django.db import models

# Create your models here.

class creategroup(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=300,blank=False)
    image=models.ImageField(upload_to='', blank=True)
    

    def __str__(self):
        return self.title