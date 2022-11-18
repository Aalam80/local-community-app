from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class catogary(models.Model):
    name= models.CharField(max_length=50)
    img =models.ImageField(upload_to='images/',default='NA')

    
    def __str__(self):
        return self.name

class services(models.Model):
    service_name=models.CharField(max_length=100)
    service_provider=models.CharField(max_length=100)
    price=models.BigIntegerField()
    contact_number=models.BigIntegerField()
    catogary=models.ForeignKey(catogary,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.service_name

class Queries (models.Model):
    Query_category=models.ForeignKey(services,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Query_detail=models.CharField(max_length=180)
    reply=models.ForeignKey('self',null=True,related_name='replies',on_delete=models.CASCADE)
   


    def __str__(self):
        return self.Query_detail



class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    Desc= models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

class serviceQuery(models.Model):
    sno=models.AutoField(primary_key= True)
    Query_Detail=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Service=models.ForeignKey(services,on_delete=models.CASCADE)
    parant=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Query_Detail

class banner(models.Model):
     imgg =models.ImageField(upload_to='images/')
