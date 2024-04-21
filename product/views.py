from django.shortcuts import render
from django.views import View
from .models import Product


class ShopPageView(View):
    def get(self, request):
        products = Product.objects.all()
        order_products = products.order_by('-rating')
        discount_product = products.filter(discount__in=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
        discount_price = []
        for product in discount_product:
            discount_price.append((product.price - product.price * int(product.discount) / 100))

        context = {
            "products": products,
            "order_products": order_products,
            "discount_product": discount_product,
            "discount_price": discount_price,
        }
        return render(request, "main/shop.html", context)
