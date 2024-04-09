from django.contrib import admin

from .models import Menu, MenuNode


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    list_display_links = ('id',)
    
    
@admin.register(MenuNode)
class MenuNodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_name',
        'url_name',
    )
    list_editable = (
        'display_name',
        'url_name',
    )
    list_display_links = ('id',)
