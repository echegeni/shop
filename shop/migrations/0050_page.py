# Generated by Django 2.2.14 on 2021-01-09 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0049_auto_20201203_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='اسلاگ')),
                ('decsription', models.TextField(max_length=300, verbose_name='مختصر توضیحات')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'برگه',
                'verbose_name_plural': 'برگه ها',
            },
        ),
    ]
