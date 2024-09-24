from django.db import models

# Create your models here.

class user(models.Model) :
    seq = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    point = models.IntegerField()
    reg_dt = models.DateTimeField(auto_now=True)
    del_user = models.IntegerField(default=0)
    purchase = models.IntegerField()
    birth = models.CharField(max_length=8)
    agree = models.IntegerField(default=0)
    
class admin(models.Model) :
    email = models.CharField(max_length=30)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
                             
class product(models.Model) :
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cnt = models.IntegerField()
    price = models.IntegerField()
    category = models.IntegerField()
    image = models.ImageField(null=True, upload_to="", blank=True)
    detail = models.TextField()
    reg_dt = models.DateTimeField(auto_now=True)
    view_cnt = models.IntegerField()
    sell_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    
class category(models.Model) :
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
class basket(models.Model) :
    seq = models.AutoField(primary_key=True)
    user_seq = models.IntegerField()
    product_seq = models.IntegerField()
    cnt = models.IntegerField()
    order = models.IntegerField(default=0)
    
class like(models.Model) :
    seq = models.AutoField(primary_key=True)
    user_seq = models.IntegerField()
    product_seq = models.IntegerField()
    
class order(models.Model) :
    seq = models.AutoField(primary_key=True)
    user_seq = models.IntegerField()
    product_seq = models.IntegerField()
    cnt = models.IntegerField()
    payment = models.IntegerField()
    invoice = models.CharField(max_length=255)
    order_dt = models.DateTimeField(auto_now=True)
    order_price = models.IntegerField()
    delivery = models.IntegerField(default=0)
    
class cs(models.Model) :
    seq = models.AutoField(primary_key=True)
    user_seq = models.IntegerField()
    product_seq = models.IntegerField()
    cs_no = models.IntegerField()
    pw = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.ImageField(null=True, upload_to="", blank=True)
    reg_dt = models.DateTimeField(auto_now=True)
    secret = models.IntegerField(default=0)
    view_cnt = models.IntegerField()
    reply = models.TextField()
    reply_dt = models.DateTimeField(auto_now=True)
    reply_check = models.IntegerField(default=0)