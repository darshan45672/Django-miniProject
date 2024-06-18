from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cartSummary(request):
    cart = Cart(request)

    cartProducts = cart.get_products 
    quantites = cart.get_quantity 
    return render(request, "cartSummary.html", {"productsInCart": cartProducts, "quantities": quantites})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity = product_quantity)

        cartQuantity = cart.__len__()

        # response = JsonResponse({"Product Name: ": product.name})
        response = JsonResponse({"Quantity: ": cartQuantity})

        return response    

def cartDelete(request):
    pass

def cartUpdate(request):
    pass