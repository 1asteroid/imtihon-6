from django.shortcuts import render
from django.views import View
from product.models import Product
from .models import Basket, BasketItems


class LandingPageView(View):
    def get(self, request):
        products = Product.objects.all()
        order_products = products.order_by('-rating')
        context = {
            "products": products,
            "order_products": order_products,
        }
        return render(request, "main/index.html", context)

    def post(self, request):
        search = request.POST["search"]
        products = Product.objects.all()
        order_products = products.order_by('-rating')
        if search:
            search_product = products.filter(name__icontains=search)
            context = {
                "products": search_product,
                "order_products": order_products,
            }
        else:
            context = {
                "products": products,
                "order_products": order_products,
            }
        return render(request, "main/index.html", context)


class NotFound404View(View):
    def get(self, request):
        login_url = ".erls"
        return render(request, "main/404.html")


class CheckOutView(View):
    def get(self, request):
        return render(request, "main/chackout.html")


class TestimonialPageView(View):
    def get(self, request):
        return render(request, "main/testimonial.html")


class CartPageView(View):
    def get(self, request, id):  # id -> user_id
        basket = Basket.objects.filter(user=id['id'])
        print(f"-------------{basket}")

        if object in basket:
            new_basket_add = Basket(user_id=id["id"])
            new_basket_add.save()

        basket_find = Basket.objects.filter(user=id["id"])[0]

        new_basket_items = BasketItems(basket=basket_find.id, user=id)
        new_basket_items.save()
        return render(request, "cart_name")


class ContactPageView(View):
    def get(self, request):
        return render(request, "main/contact.html")


class ShopDetailsView(View):
    def get(self, request, id):
        products = Product.objects.all()
        product = products.get(id=id)
        context = {
            "product": product,
            "products": products
        }
        print(product)
        return render(request, "main/shop-detail.html", context)
