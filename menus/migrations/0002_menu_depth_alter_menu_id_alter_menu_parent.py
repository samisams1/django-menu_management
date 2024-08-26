# Generated by Django 5.1 on 2024-08-24 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='depth',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menus.menu'),
        ),
    ]
