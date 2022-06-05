from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product


@require_POST
def cartAdd(request, productId):
    cart = Cart(request)
    product = get_object_or_404(Product, id=productId)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], updateQuantity=cd['update'])
    return redirect('cart:cartDetail')


def cartRemove(request, productId):
    cart = Cart(request)
    product = get_object_or_404(Product, id=productId)
    cart.remove(product)
    return redirect('cart:cartDetail')


def cartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['upDateQuantityForm'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
