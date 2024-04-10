from django.urls import path

from .views import (
    index_view,
    example_view,
)


urlpatterns = [
    #---- примеры URL для первого меню:
    path('v1/main/', index_view, name='index'),
    path('v1/main/profile/', example_view, name='profile'),
    path('v1/main/profile/settings/', example_view, name='settings'),
    path('v1/main/profile/settings/privacy/', example_view, name='privacy'),
    path('v1/main/profile/settings/personal-info/', example_view, name='personal'),
    path('v1/main/profile/photos/', example_view, name='photos'),
    path('v1/main/profile/other/', example_view, name='other'),
    path('v1/main/contacts/', example_view, name='contacts'),
    path('v1/main/products/', example_view, name='products'),
    #---- примеры URL для второго меню:
    path('v2/main/', index_view, name='index2'),
    path('v2/main/profile/', example_view, name='profile2'),
    path('v2/main/profile/settings/', example_view, name='settings2'),
    path('v2/main/profile/settings/privacy/', example_view, name='privacy2'),
    path('v2/main/profile/settings/personal-info/', example_view, name='personal2'),
    path('v2/main/profile/photos/', example_view, name='photos2'),
    path('v2/main/profile/other/', example_view, name='other2'),
    path('v2/main/contacts/', example_view, name='contacts2'),
    path('v2/main/products/', example_view, name='products2'),
]
