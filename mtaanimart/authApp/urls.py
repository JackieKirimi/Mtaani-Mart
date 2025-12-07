from django.urls import path, include
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('payment', views.mpesaPayment, name='mpesaPayment'),
    path("checkout/", views.checkout, name="checkout"),
    #path("delivery/", views.delivery_map, name="delivery_map"),
    #path("add-delivery/", views.add_delivery_location, name="add_delivery"),


]
