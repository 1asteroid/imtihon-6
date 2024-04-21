from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)


class BasketItems(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # shu mahsulotdan necha kg ekanligi
    slug = models.SlugField(verbose_name="slug", max_length=100, null=False)

    def __str__(self):
        return f"{self.basket}-{self.product}"
