from django.shortcuts import render
from django.views import View
from product.models import Product
from django.contrib.auth.models import User
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
    def get(self, request, id):
        basket = Basket.objects.filter(user=id)
        print(f"-------------{basket}")

        if object in basket:
            new_basket_add = Basket(user_id=id)
            new_basket_add.save()
            print("----kirdi")

        basket_find = Basket.objects.filter(user=id)[0]

        basket_items = BasketItems.objects.filter(basket=basket_find.id)

        def product_id(quereset):
            product_id_list = []
            if not (object in quereset):
                for i in quereset:
                    product_id_list.append(i.id)
            return product_id_list

        products = Product.objects.filter(pk__in=product_id(basket_items))
        print(product_id(basket_items))
        print(f"-------------{basket_items}")
        context = {
            "products": products
        }
        print(products)
        return render(request, "main/cart.html", context)


class ContactPageView(View):
    def get(self, request):
        return render(request, "main/contact.html")
