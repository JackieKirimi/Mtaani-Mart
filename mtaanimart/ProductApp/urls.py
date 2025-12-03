from django.urls import path
from . import views

urlpatterns = [
    path('produts/', views.productStore)
]

