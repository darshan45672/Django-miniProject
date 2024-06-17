from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cartSummary(request):
    return render(request, "cartSummary.html", {})

def cartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        cartQuantity = cart.__len__()

        # response = JsonResponse({"Product Name: ": product.name})
        response = JsonResponse({"Quantity: ": cartQuantity})

        return response    

def cartDelete(request):
    pass

def cartUpdate(request):
    pass