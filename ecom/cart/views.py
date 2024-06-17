from django.shortcuts import render

def cartSummary(request):
    return render(request, "cartSummary.html", {})

def cartAdd(request):
    pass

def cartDelete(request):
    pass

def cartUpdate(request):
    pass