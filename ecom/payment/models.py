from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shippingFullName = models.CharField(max_length=200, null=False, blank=False)
    shippingEmail = models.CharField(max_length=200, null=False, blank=False)
    shippingAddress1 = models.CharField(max_length=200, null=False, blank=False)
    shippingAddress2 = models.CharField(max_length=200, null=True, blank=True)
    shippingCity = models.CharField(max_length=200, null=False, blank=False)
    shippingState = models.CharField(max_length=200, null=False, blank=False)
    shippingZipcode = models.CharField(max_length=200, null=False, blank=False)
    shippingCountry = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}' 