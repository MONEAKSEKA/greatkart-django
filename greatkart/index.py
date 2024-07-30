from django.shortcuts import render
from store.models import Product

def home(request):
    #Query only products have in stock
    products = Product.objects.all().filter(is_available=True)

    #Store as a temporary in a dictionary
    context = {
        'products': products,
    }

    return render(request, 'home.html', context)