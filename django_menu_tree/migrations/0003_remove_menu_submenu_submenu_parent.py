# Generated by Django 4.1.7 on 2023-03-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_menu_tree', '0002_submenu_remove_menu_parent_menu_submenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='submenu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='django_menu_tree.menu', verbose_name='Меню'),
        ),
    ]
