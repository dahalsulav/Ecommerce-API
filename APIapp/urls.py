from django.urls import path
from APIapp.views import *
urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('category/<int:pk>/',DetailCategory.as_view(),name='singleCategory'),
    path('books',ListBook.as_view(),name='books'),
    path('book/<int:pk>/',DetailBook.as_view(),name='singleBook'),
    path('products',ListProduct.as_view(),name='products'),
    path('product/<int:pk>/',DetailProduct.as_view(),name='singleProduct'),
]
