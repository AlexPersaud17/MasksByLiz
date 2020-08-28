from django.db import models
from django.urls import reverse



class Product(models.Model):
    mainimage = models.ImageField()
    name = models.CharField(max_length=300)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()

    def __str__(self):
        return self.name



class Cart(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
