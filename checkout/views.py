from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bagat the moment")
        return redirect(reverse('product'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MQTXfFQfyIQwd2rNIKjSBxtkYOAcVItkQKeo7IYFcwNrDAJwtuZpKGqxiNOrxkSYx8FqWP0J0vQYzHJKxkc3A2D00kHeRGy6h',  # noqa E501
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
