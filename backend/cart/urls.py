from . import views
from django.urls import path

urlpatterns = [
    path(route="", view=views.cart_view, name="cart-view"),
]
