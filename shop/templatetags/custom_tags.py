from django import template
from django.db.models import Sum
from django.urls import reverse
from shop.models import Category
register = template.Library()


@register.simple_tag
def my_slice(input):
    if len(input) > 30:
        return input[0:30] + "..."
    else:
        return input


