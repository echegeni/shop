# Generated by Django 2.2.14 on 2020-11-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_category_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='child',
        ),
    ]
