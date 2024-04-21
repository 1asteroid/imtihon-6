import uuid
from django.db.models import TextChoices


class SaveImages(object):
    def product_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/{uuid.uuid4()}.{image_extension}"


class ProductChoiseArgument:
    class PriceType(TextChoices):
        dollor = "$", "USD"
        sum = "sum", "UZS"

    class CategoryType(TextChoices):
        vegetable = "vegetables", "vegetables"
        fruit = "fruit", "fruit"
        bread = "bread", "bread"
        meat = "meat", "meat"

    class Discount(TextChoices):
        dis0 = "0", "0%"
        dis10 = "10", "10%"
        dis20 = "20", "20%"
        dis30 = "30", "30%"
        dis40 = "40", "40%"
        dis50 = "50", "50%"
        dis60 = "60", "60%"
        dis70 = "70", "70%"
        dis80 = "80", "80%"
        dis90 = "90", "90%"
        dis100 = "100", "100%"

    class QualityType(TextChoices):
        organic = "organic", "organic"
        fresh = "fresh", "fresh"
        discount = "discount", "discount"
        expired = "expired", "expired"

    class ExpirationDateType(TextChoices):
        day = "day", 'day'
        month = "month", "month"
        year = "year", "year"
