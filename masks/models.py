from django.db import models
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=250)
    @classmethod
    def create(cls, product_name):
        item = cls(product_name=product_name)
        return item