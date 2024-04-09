from django import template

from ..models import Menu, MenuNode

register = template.Library()


@register.inclusion_tag('templatetags/menu.html')
def render_menu(request, menu_name: str) -> dict | None:
    try:
        nodes = (
            Menu.objects
            .get(name=menu_name)
            .nodes.all()
            .order_by('-is_head')
        )
    except Menu.DoesNotExist:
        return None
    
    return {'nodes': nodes, 'request': request}


@register.inclusion_tag('templatetags/menu_child.html')
def render_menu_child(request, child: MenuNode) -> dict:
    return {'child': child, 'request': request}


@register.simple_tag
def url_in_uri(url, uri) -> bool:
    return url in uri