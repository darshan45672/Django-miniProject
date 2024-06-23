from django.urls import path
from . import views

urlpatterns = [
    path('payment-success/', views.paymentSucess, name="paymentSucess"),
]