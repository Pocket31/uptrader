from django.shortcuts import render
from menu.models import Menu
# Create your views here.


def render_menu(request, menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'menu/index.html', {'menu_items': menu_items})
