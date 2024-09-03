from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

from django.urls import reverse



class catgory(models.Model):
    name=models.CharField(max_length=20)    

    def __str__(self):
        return self.name

class customer(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=22)
    email= models.CharField(max_length=220)
    PASSWORD= models.CharField(max_length=220)

    
    def __str__(self):
        return F"{self.first_name} {self.last_name}" 

class merch(models.Model):
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=100, default=True,blank=True,null=True)
    price = models.DecimalField( max_digits=12,default=0, decimal_places=2,)
    catgory=models.ForeignKey(catgory,on_delete=models.CASCADE)

    picturee=models.ImageField(upload_to='upload/product/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField( max_digits=12,default=0, decimal_places=2,)
    def __str__(self):
        return self.name


class order(models.Model):
    merch=models.ForeignKey(merch,on_delete=models.CASCADE ,default=True)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quntity=models.IntegerField(default=1,)
    addres = models.CharField(max_length=400,default="",blank=True)
    phone = models.DecimalField( max_digits=12,default=True, decimal_places=2,)
    release_date = models.DateTimeField(default=datetime.now())
    status= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.merch

# Create your models here.
