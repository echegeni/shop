# Generated by Django 2.2.14 on 2020-12-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_accounting_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='ammount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=11),
        ),
    ]
