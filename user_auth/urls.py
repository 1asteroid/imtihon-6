from django.urls import path
from .views import StudentRegisterView, StudentLoginView, UserLogOutView


urlpatterns = [
    path("register/", StudentRegisterView.as_view(), name='register'),
    path("login/", StudentLoginView.as_view(), name='login'),
    path("logout/", UserLogOutView.as_view(), name='logout'),
]
