from django.contrib import admin
from APIapp.models import Category, Book, Product
# Registering app models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)

