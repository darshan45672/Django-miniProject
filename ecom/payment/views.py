from django.shortcuts import render

def paymentSucess(request):
    return render(request, 'paymentSucess.html', {})