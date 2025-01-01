# Generated by Django 5.1.2 on 2024-11-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicename', models.CharField(max_length=50)),
                ('salonname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='null.jpg', upload_to='images')),
            ],
        ),
    ]
