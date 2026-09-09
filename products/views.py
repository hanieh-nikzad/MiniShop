from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'query': query
        }
    )


def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )


def category_products(request, id):
    category = Category.objects.get(id=id)

    products = Product.objects.filter(category=category)

    return render(
        request,
        'products/category_products.html',
        {
            'category': category,
            'products': products
        }
    )