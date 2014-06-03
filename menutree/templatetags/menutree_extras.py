# -*- coding:utf-8 -*-
from ..models import Menu, MenuItem
from django import template
from django.core.cache import cache

register = template.Library()

def build_menu(parser, token):
    """
    {% menu menu_name %}
    """
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return MenuObject(menu_name)

class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        current_path = context['request'].path
        user = context['request'].user
        context['menutree_items'] = get_items(self.menu_name, current_path, user)
        return ''
  
def build_sub_menu(parser, token):
    """
    {% submenu %}
    """
    return SubMenuObject()

class SubMenuObject(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        current_path = context['request'].path
        user = context['request'].user
        menu = False
        for m in Menu.objects.filter(base_url__isnull=False):
            
            print m.base_url
            if m.base_url and current_path.startswith(m.base_url):
                menu = m

        if menu:
            context['submenu_items'] = get_items(menu.slug, current_path, user)
            context['submenu'] = menu
        else:
            context['submenu_items'] = context['submenu'] = None
        return ''

def get_items(menu_name, current_path, user):
    """
    If possible, use a cached list of items to avoid continually re-querying 
    the database.
    The key contains the menu name, whether the user is authenticated, and the current path.
    Disable caching by setting MENU_CACHE_TIME to -1.
    """

    from django.conf import settings
    cache_time = getattr(settings, 'MENU_CACHE_TIME', 1800)
    debug = getattr(settings, 'DEBUG', False)

    if cache_time >= 0 and not debug:
        cache_key = 'django-menutree-items/%s/%s'  % (menu_name, current_path)
        menuitems = cache.get(cache_key, [])
        if menuitems:
            return menuitems
    else:
        menuitems = []

    try:
        menu = Menu.objects.get(slug=menu_name)
    except Menu.DoesNotExist:
        raise template.TemplateSyntaxError, "Not found menutree item with slug = %r" % menu_name

    for i in MenuItem.objects.filter(menu=menu, parent=None).order_by('order'):
        children = i.get_children()

        for child in children:
            child.link_url = i.link_url.rstrip('/') + '/' + child.link_url.lstrip('/')
        

        current = ( i.link_url != '/' and current_path.startswith(i.link_url)) or ( i.link_url == '/' and current_path == '/' )
        menuitems.append({'link_url': i.link_url, 'title': i.title, 'current': current, 'children': children, })

    if cache_time >= 0 and not debug:
        cache.set(cache_key, menuitems, cache_time)
    return menuitems

register.tag('menutree', build_menu)