from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # if the cart object does not exist in self.session, initialize one
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        productIds = self.cart.keys()
        products = Product.objects.filter(id__in=productIds)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            '''
            keys in item:
            product, quantity, price, totalPrice            
            '''
            item['price'] = Decimal(item['price'])
            item['totalPrice'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # the number of products
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, updateQuantity=False):
        # Add items to the shopping cart or update the number of items in the shopping cart
        productId = str(product.id)
        if productId not in self.cart:
            self.cart[productId] = {'quantity': 0, 'price': str(product.price)}
        if updateQuantity:
            self.cart[productId]['quantity'] = quantity
        else:
            self.cart[productId]['quantity'] += quantity
        self.save()

    def remove(self, product):
        productId = str(product.id)
        if productId in self.cart:
            del self.cart[productId]
            self.save()

    def save(self):
        # If the session.modified value is set to True, the session will be saved
        # when the middleware sees this property.
        self.session.modified = True

    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


