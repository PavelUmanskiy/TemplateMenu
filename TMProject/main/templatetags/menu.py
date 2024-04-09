from django import template

from ..models import Menu, MenuNode

register = template.Library()


@register.inclusion_tag('templatetags/menu.html')
def render_menu(menu_name: str) -> dict | None:
    try:
        nodes = (
            Menu.objects
            .get(name=menu_name)
            .nodes.all()
            .order_by('is_head').desc()
        )
        x = MenuNode.objects.all().__getitem__
    except Menu.DoesNotExist:
        return None
    
    return {'nodes': nodes}


@register.inclusion_tag('templatetags/menu_child.html')
def render_menu_child(child: MenuNode) -> dict:
    return {'child': child}
