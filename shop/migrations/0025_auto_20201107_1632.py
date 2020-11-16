# Generated by Django 2.2.14 on 2020-11-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20201107_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Category', verbose_name='زیر دسته'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
        migrations.RemoveField(
            model_name='category',
            name='child',
        ),
    ]
