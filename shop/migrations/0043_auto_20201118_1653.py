# Generated by Django 2.2.14 on 2020-11-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20201118_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop_name',
            name='products',
        ),
        migrations.AlterField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Province', verbose_name='شهر'),
        ),
    ]