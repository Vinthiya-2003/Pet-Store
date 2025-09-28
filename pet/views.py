from django.shortcuts import render

# Main Pages
def home(request):
    return render(request, 'pet/home.html')

def about(request):
    return render(request, 'pet/about.html')

def contact(request):
    return render(request, 'pet/contact.html')

def shop(request):
    return render(request, 'pet/shop.html')

def login_view(request):
    return render(request, 'pet/login.html')

def cart(request):
    return render(request, 'pet/cart.html')

def checkout(request):
    return render(request, 'pet/checkout.html')

def back(request):
    return render(request, 'pet/back.html')


# Sub Navigation Pages
def dog(request):
    return render(request, 'pet/dog.html')

def cat(request):
    return render(request, 'pet/cat.html')

def small_pets(request):
    return render(request, 'pet/small_pets.html')

def pet_service(request):
    return render(request, 'pet/pet_service.html')

def shop_by_brand(request):
    return render(request, 'pet/shop_by_brand.html')

def shop_by_breed(request):
    return render(request, 'pet/shop_by_breed.html')

def consult_vet(request):
    return render(request, 'pet/consult_vet.html')
