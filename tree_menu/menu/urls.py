from django.urls import path
from menu.views import render_menu

app_name = 'menu'

urlpatterns = [
    path('<str:menu_name>/', render_menu, name='render_menu'),
]
