from django.urls import path

from .views import (
    index_view,
    example_view,
)


urlpatterns = [
    path('main/', index_view, name='index'),
    path('main/profile/', example_view, name='profile'),
    path('main/profile/settings/', example_view, name='settings'),
    path('main/profile/settings/privacy/', example_view, name='privacy'),
    path('main/profile/settings/personal-info/', example_view, name='personal'),
    path('main/profile/photos/', example_view, name='photos'),
    path('main/profile/other/', example_view, name='other'),
    path('main/contacts/', example_view, name='contacts'),
    path('main/products/', example_view, name='products'),  
]
