from django.contrib import admin
from .models import Category, Customer, Product, Order,Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmine(admin.ModelAdmin):
    model = User
    field = ["username", "firstName", "lastName", "email"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmine)