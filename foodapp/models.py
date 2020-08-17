from django.db import models
from django.contrib.auth.models import User


class regdata(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    pswrd = models.CharField(max_length=60,) 

    def __str__(self):
        return self.name

class fooditem(models.Model):
    name = models.CharField(max_length=100,)
    description = models.CharField(max_length=700,)

    price = models.IntegerField()
    img = models.ImageField(upload_to="gallery")
    def __str__(self):
        return self.name

class cartitem(models.Model):
    userob = models.ForeignKey(User, on_delete=models.CASCADE)
    id1 = models.IntegerField()

    count = models.IntegerField()

class address(models.Model):
    userob = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    streetad = models.CharField(max_length=500)
    pincode = models.IntegerField()

class state(models.Model):
    state=models.CharField(max_length=50)
    def __str__(self):
        return self.state

class discount(models.Model):
    code=models.CharField(max_length=50,unique=True)
    percentdisc=models.IntegerField()

class order(models.Model):
    username = models.CharField(max_length=100)
    
    addressid = models.IntegerField()
    price = models.IntegerField(default=0)
    
    paying_online = models.BooleanField(default=False)
    order_active = models.BooleanField(default=False)
    pay_status = models.BooleanField(default=False)
    order_delivered = models.BooleanField(default=False)
    order_status=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.id
    

class indvdl_order(models.Model):
    orderparent=models.ForeignKey(order, on_delete=models.CASCADE)
    count=models.IntegerField()
    foodid=models.IntegerField()
    price=models.IntegerField()