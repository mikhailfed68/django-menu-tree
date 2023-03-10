# Generated by Django 4.1.7 on 2023-03-02 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_menu_tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.AddField(
            model_name='menu',
            name='submenu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='django_menu_tree.submenu', verbose_name='Подменю'),
        ),
    ]
