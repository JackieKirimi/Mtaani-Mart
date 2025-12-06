from django.db import models
from django.contrib.auth.models import User


# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# CartItem model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # 👈 now properly inside the class
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"