from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def productList(request, categorySlug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('name')
    if categorySlug:
        category = categories.filter(slug=categorySlug)[0]
        products = products.filter(category=category)

    contexts = {'category': category, 'categories': categories, 'products':products}
    return render(request, 'shop/product/list.html', contexts)


def productDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cartProductForm = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product':product, 'cartProductForm':cartProductForm})
