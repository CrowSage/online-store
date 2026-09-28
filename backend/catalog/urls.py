from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.category_list, name="category_list"),
    path("", views.product_list, name="product_list"),
    path("<slug:slug>/", views.product_detail, name="product-detail"),
]
