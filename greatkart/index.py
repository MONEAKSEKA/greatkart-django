from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    #Query only products have in stock
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    #Store as a temporary in a dictionary
    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)