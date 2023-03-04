from django.contrib import admin

from django_menu_tree import models


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    search_help_fields = 'Начните поиск по названию меню'
    autocomplete_fields = ('parent',)
    prepopulated_fields = {'use_named_url': True}
    list_per_page = 10
