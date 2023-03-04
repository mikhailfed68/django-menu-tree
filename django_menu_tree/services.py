from django.urls import reverse

from django_menu_tree.models import Menu


def get_menu_from_db(menu_name):
    return Menu.objects.raw(
        f"""
        WITH RECURSIVE r AS (
            SELECT id, parent_id, name, url, use_named_url, 1 AS level
            FROM django_menu_tree_menu
            WHERE name = '{menu_name}'

            UNION ALL

            SELECT django_menu_tree_menu.id, django_menu_tree_menu.parent_id, django_menu_tree_menu.name, django_menu_tree_menu.url, django_menu_tree_menu.use_named_url, r.level + 1 AS level
            FROM django_menu_tree_menu
                JOIN r
                    ON django_menu_tree_menu.parent_id = r.id
        )

        SELECT * FROM r ORDER BY level ASC;
        """
    )


def build_named_url(node, named_url):
    if node.use_named_url and named_url is not None:
        return reverse(named_url, kwargs={'pk': node.id})
    return node.url


def record(tree, submenu):
    if tree.get(str(submenu.parent_id)):
        tree[str(submenu.parent_id)]['children'][str(submenu.id)] = dict(
            id=submenu.id,
            name=submenu.name,
            url=submenu.url,
            use_named_url=submenu.use_named_url, 
            children={},
        )
        return tree

    for key, node in tree.items():
        node['children'] = record(node['children'], submenu)
        node[key] = node
    return tree


def build_menu_tree(menu, request):
    menu_tree = {}

    for submenu in menu:
        submenu.url = build_named_url(submenu, request)

        if submenu.parent_id == None:
            menu_tree[str(submenu.id)] = dict(
                id=submenu.id,
                name=submenu.name,
                url=submenu.url,
                use_named_url=submenu.use_named_url,
                children={},
            )
        else:
            menu_tree = record(menu_tree, submenu)
    return menu_tree