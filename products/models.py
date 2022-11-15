from django.db import models

# Create your models here.


class Products(models.Model):
    """these class helps to make products.
    """
    item_name = models.CharField(max_length=100, unique=True)
    unit = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        """refer entire class as given user attributes"""
        return self.item_name


class StorMaster(models.Model):
    """a stor master can tack multiple products.
    """
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    stor_master_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)

    def __str__(self):
        """refer entire class as given user attributes"""
        return self.stor_master_name


class ProductMaster(models.Model):
    """product master tack products details"""
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_master_name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        """refer entire class as given user attributes"""
        return self.product_master_name
