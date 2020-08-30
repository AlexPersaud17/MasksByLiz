from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    mainimage = models.ImageField()
    name = models.CharField(max_length=300)
    detail_text = models.TextField(max_length=1000)
    price = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def get_total(self):
        total = self.item.price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_totals(self):
            total = 0
            for order_item in self.orderitems.all():
                total += order_item.get_total()
            
            return total