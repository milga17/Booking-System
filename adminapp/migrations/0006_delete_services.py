# Generated by Django 5.1.2 on 2024-11-27 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_remove_services_sname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
    ]
