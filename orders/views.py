from django.shortcuts import render, redirect
from .forms import OrderForm
from products.models import Product
from .models import OrderItem


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            cart = request.session.get("cart", {})

            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price,
                )

            request.session["cart"] = {}

            return redirect("order_success", order_id=order.id)

    else:
        form = OrderForm()

    return render(
        request,
        "orders/create_order.html",
        {"form": form},
    )


def order_success(request, order_id):
    return render(
        request,
        "orders/order_success.html",
        {"order_id": order_id},
    )