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

class orderitem(admin.ModelAdmin):
    list_filter = ('shop','order')
    list_display = ('order','shop','get_cost')

class Accounting(admin.ModelAdmin):
    list_display = ('shop','order')
    def sumsell(self, obj,OrderItem):
        price = models.OrderItem.objects.get()
            


admin.site.register(models.Category,DraggableMPTTAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.FileGallery)
admin.site.register(models.Order)
admin.site.register(models.PaymentLog)
admin.site.register(models.OrderItem,orderitem)
admin.site.register(models.Comment)
admin.site.register(models.Shop_name)
admin.site.register(models.page)
admin.site.register(models.slider)
admin.site.register(models.banner)
admin.site.register(models.Accounting,Accounting)
