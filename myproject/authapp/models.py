from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    # confirm=models.CharField(max_length=10)

class Address(models.Model):
    address=models.CharField(max_length=40)
    adress_2=models.CharField(max_length=40)
    city=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
CATEGORY_CHOICES=(
    ('S','SWEET'),
    ('N','NAMKEEN'),
    ('M','MEALS'),
    ('B','BAKERY')
)
BRAND_CHOICES=(
    ('J','JHULELAL'),
    ('A','APNASWEET'),
    ('S','SAFFRON'),
    ('M','MISHRI')
)
STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')

)
class Product(models.Model):
    item_name=models.CharField(max_length=30)
    item_price=models.FloatField(max_length=30)
    item_brand=models.CharField(choices=BRAND_CHOICES,max_length=1)
    item_category=models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    item_image=models.ImageField(upload_to="product/",default='mixture.png')
    def __str__(self):
        return self.item_name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.item_price
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity*self.product.item_price