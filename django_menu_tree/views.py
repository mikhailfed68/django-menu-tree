from django.views.generic import DetailView

from django_menu_tree.models import Menu


class MenuView(DetailView):
    model = Menu
