from django import template

from ..models import MenuNode


register = template.Library()


@register.inclusion_tag('templatetags/menu.html')
def render_menu(request, menu_name: str) -> dict | None:
    try:
        nodes = (
            MenuNode.objects
            .filter(menu_name=menu_name)
            .select_related('parent')
            .order_by('-is_head')
        )
    except MenuNode.DoesNotExist:
        return None
    
    def populate_children(nodes_to_populate, global_nodes):
        for node in nodes_to_populate:
            node.all_children = list(filter(lambda n: n.parent==node, global_nodes))
            if node.all_children:
                populate_children(node.all_children, global_nodes)
    # Тут мы вынуждены немного побороться с Джанго чтобы не хитать бд лишний раз
    # Суть проблемы: все нужные ноды есть, но если пользоваться встроенными
    # инструментами Джанго, будет лишний хит по бд при вызове render_menu_child.
    # Моё решение: самостоятельно рекурсивно разложить детей по родителям
    populate_children(nodes, list(nodes).copy()) 
    return {'nodes': list(nodes), 'request': request}


@register.inclusion_tag('templatetags/menu_child.html')
def render_menu_child(request, nodes, child: MenuNode) -> dict:
    return {'child': child, 'request': request, 'nodes': nodes}


@register.simple_tag
def url_in_uri(url, uri) -> bool:
    return url in uri
