from django.urls import path, include
from . import views
from django.urls import path



urlpatterns = [
    path('index',views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('payment', views.mpesaPayment, name='mpesaPayment'),
    path("checkout/", views.checkout, name="checkout"),
    path("help/", views.help_page, name="help"),
   
]