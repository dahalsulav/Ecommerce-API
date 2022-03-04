from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=200, default="Unknown")
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '{} - {}'.format(self.product_tag,self.name) 