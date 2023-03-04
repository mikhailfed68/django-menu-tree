Django-menu-tree
=====

Django-menu-tree is a Django app for creating menus and storing them in a database.
It allows you to retrieve the entire tree menu in one query to the database.


Quick start
-----------

1. Add "django_menu_tree" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
    
        ...
        'django_menu_tree',
        
    ]

2. Create a template, for example, a base template in your root:

    `templates/base.html` 

    If you have created such a structure you also need update settings.py in your TEMPLATES variable:

    `'DIRS': ['templates'],`

3. Include the django_menu_tree URLconf in your project-level urls.py like this:

    `from django_menu_tree.views import MenuView`

    `path('category/<int:pk>/', MenuView.as_view(template_name='base.html'), name='menu'),`

4. Add the following to your templates/base.html like this:

    `{% load menus %}`

    `{% draw_menu menu_name='<name menu>' named_url='menu' %}`

    `{% block content %}{% endblock %}` _(if you use base template)_

    named_url is optional if you only use custom urls in menu.
    You can also use `app_name:named_url` format.

4. Run `python manage.py migrate` to create the models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a menus (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/category/<int:pk>/ to view menu tree.
