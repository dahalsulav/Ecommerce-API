from rest_framework import serializers
from APIapp.models import Category, Book, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'title'
        )
        model = Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'title', 'category','author', 'isbn', 'pages', 'price', 'description', 'imageUrl', 'status', 'created_date'
        )
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id','product_tag','name','category','price','stock','imageUrl','status','created_date'
        )
        model = Product