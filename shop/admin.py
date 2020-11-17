from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from shop import models
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.ImageGallery)
admin.site.register(models.City)
admin.site.register(models.Province)


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(models.Category,DraggableMPTTAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.FileGallery)
admin.site.register(models.Order)
admin.site.register(models.PaymentLog)
admin.site.register(models.OrderItem)
admin.site.register(models.Comment)
admin.site.register(models.Shop_name)
