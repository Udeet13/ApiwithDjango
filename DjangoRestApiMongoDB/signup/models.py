from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length =30, blank=False,default='')
    email = models.CharField(max_length=50,blank=False,default = '')
    password = models.CharField(max_length=36,blank=False)
    