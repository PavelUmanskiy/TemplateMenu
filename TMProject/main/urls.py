from django.urls import path

from .views import (
    index_view,
    example_view,
    example_detail_view
)


urlpatterns = [
    path('home/', index_view, name='index'),
    path('home/profile/', example_view, name='profile'),
    path('home/contacts/', example_view, name='contacts'),
    path('home/products/', example_view, name='products'),
    path('home/products/<int:pk>/', example_detail_view, name='product_detail'),    
]
