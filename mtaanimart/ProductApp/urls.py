from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("cart/", views.cart, name="cart"),
    path("remove_from_cart/<int:item_id>/", views.remove_from_cart, name='remove_from_cart'),
  

]

