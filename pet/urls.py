from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('login/', views.login_view, name="login"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('back/', views.back, name="back"),
  


    # Sub Navigation
    path('dog/', views.dog, name="dog"),
    path('cat/', views.cat, name="cat"),
    path('small-pets/', views.small_pets, name="small_pets"),
    path('pet-service/', views.pet_service, name="pet_service"),
    path('shop-by-brand/', views.shop_by_brand, name="shop_by_brand"),
    path('shop-by-breed/', views.shop_by_breed, name="shop_by_breed"),
    path('consult-vet/', views.consult_vet, name="consult_vet"),
]
