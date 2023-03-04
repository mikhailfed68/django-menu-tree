# Generated by Django 4.1.7 on 2023-03-02 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_menu_tree', '0003_remove_menu_submenu_submenu_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='django_menu_tree.menu', verbose_name='Подменю'),
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
    ]
