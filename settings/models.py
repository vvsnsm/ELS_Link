from django.db import models

# Create your models here.
class userinfo(models.Model):
    fname = models.CharField(max_length=40,default='SOME STRING' )
    lname = models.CharField(max_length=40,default='SOME STRING' )
    username = models.CharField(max_length=15,default='SOME STRING' )
    def __str__(self):
        return self.username