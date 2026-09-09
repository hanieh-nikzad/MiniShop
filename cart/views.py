from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def cart_detail(request):
    cart = request.session.get("cart", {})

    product_ids = cart.keys()

    products = Product.objects.filter(id__in=product_ids)

    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        product.total = product.price * quantity
        total_price += product.price * quantity

    return render(
        request,
        "cart/cart_detail.html",
        {
            "products": products,
            "cart": cart,
            "total_price": total_price,
        },
    )


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["cart"] = cart

    return redirect("cart_detail")

def increase_quantity(request, product_id):
    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session["cart"] = cart

    return redirect("cart_detail")


def decrease_quantity(request, product_id):
    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session["cart"] = cart

    return redirect("cart_detail")









def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart

    return redirect("cart_detail")