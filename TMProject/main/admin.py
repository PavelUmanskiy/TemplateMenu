from django.contrib import admin

from .models import MenuNode

 
@admin.register(MenuNode)
class MenuNodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_name',
        'url_name',
        'menu_name',
    )
    list_editable = (
        'display_name',
        'url_name',
        'menu_name',
    )
    list_display_links = ('id',)
