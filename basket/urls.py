from django.urls import path
from .views import LandingPageView, NotFound404View, CheckOutView, TestimonialPageView, CartPageView, ContactPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('not-found/', NotFound404View.as_view(), name='not_found'),
    path('check-out/', CheckOutView.as_view(), name='check_out'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('cart/<int:id>', CartPageView.as_view(), name='cart'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
