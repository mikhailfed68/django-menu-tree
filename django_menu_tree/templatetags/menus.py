from django.template import Library

from django_menu_tree import services

register = Library()


@register.inclusion_tag('django_menu_tree/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name, named_url=None):
    request = context['request']
    menu = services.get_menu_from_db(menu_name)
    menu_tree = services.build_menu_tree(menu, named_url)
    return dict(menu=menu_tree, request=request)
