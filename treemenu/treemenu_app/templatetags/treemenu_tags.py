from django import template
from django.db.models import Prefetch

from treemenu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, slug):

    def construct_submenu(menu):
        children = {}
        active = menu.url == url
        for item in menu.items.all():
            child = construct_submenu(item)
            children[item] = child
            if child['active']:
                active = True

        return {
            'children': children,
            'active': active
        }

    menu = MenuItem.objects.get(slug=slug)
    url = context['request'].path

    return {'menutree': {menu: construct_submenu(menu)}}


@register.inclusion_tag('draw_menu.html')
def draw_submenu(menutree):
    return {'menutree': menutree}
