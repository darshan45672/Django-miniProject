from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cartSummary(request):
    cart = Cart(request)

    cartProducts = cart.get_products 
    quantites = cart.get_quantity 
    cartTotals = cart.total()
    return render(request, "cartSummary.html", {"productsInCart": cartProducts, "quantities": quantites, "total": cartTotals})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity = product_quantity)

        cartQuantity = cart.__len__()

        # response = JsonResponse({"Product Name: ": product.name})
        messages.success(request, ("Product added to cart"))
        response = JsonResponse({"Quantity: ": cartQuantity})

        return response    

def cartUpdate(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product = product_id, quantity = product_quantity)
        response = JsonResponse({'Quantity': product_quantity})
        messages.success(request, ("Product quantity updated"))

        return response

def cartDelete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product = product_id)

        response = JsonResponse({'Deleted Product': product_id})
        messages.success(request, ("Product deleted from cart"))

        return response