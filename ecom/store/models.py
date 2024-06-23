from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dateModified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    oldCart = models.CharField(max_length=200 ,blank=True, null=True)

    def __str__(self):
        return self.user.username

def createProfile(sender,instance,created, **kwargs):
    if created:
        userProfile = Profile(user = instance)
        userProfile.save()

post_save.connect(createProfile, sender=User, )

#Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural ='categories'

# customer or user model
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{ self.firstName} { self.lastName}'

# product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price =  models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    image =  models.ImageField(upload_to='uploads/product/')

    is_sales = models.BooleanField(default=False)
    salePrice = models.DecimalField(default=0, decimal_places=2, max_digits=7)

    
    def __str__(self):
        return f'{self.name}' 

# Order model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=300, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product