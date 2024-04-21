from django.db import models
from .helpes import SaveImages, ProductChoiseArgument


class Category(models.Model):
    name = models.CharField(max_length=30, default="fruit")


class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(verbose_name="slug", max_length=100, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to=SaveImages.product_images_path)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_type = models.CharField(max_length=10, choices=ProductChoiseArgument.PriceType.choices,
                                  default=ProductChoiseArgument.PriceType.dollor)
    category = models.CharField(max_length=20, choices=ProductChoiseArgument.CategoryType.choices,
                                default=ProductChoiseArgument.CategoryType.fruit)
    discount = models.CharField(choices=ProductChoiseArgument.Discount.choices,
                                default=ProductChoiseArgument.Discount.dis0)
    quality = models.CharField(max_length=10, choices=ProductChoiseArgument.QualityType.choices,
                               default=ProductChoiseArgument.QualityType.organic)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
