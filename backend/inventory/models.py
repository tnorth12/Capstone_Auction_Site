from django.db import models;
from authentication.models import User;
from django.db.models.fields import BLANK_CHOICE_DASH;

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    image = models.ImageField(null=True,blank = True,default = "/images/placeholder.png",upload_to="images/")
    _id = models.AutoField(primary_key=True,editable=False)
    brand = models.CharField(max_length=255)     
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name +" | "+self.brand +" | " + str(self.price)
        

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    # order  = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    # qty = models.IntegerField(null=True,blank=True,default=0)
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    image = models.CharField(max_length=200,null=True,blank=True)
    _id =  models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)