from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=21)
    joined_date = models.DateField(null=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.name} {self.price}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=21)
    date = models.DateField()
    status = models.BooleanField()