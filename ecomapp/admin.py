from django.contrib import admin
from ecomapp.models import Product
# Register your models here.
#admin.site.register(Product)

#define ModelAdminClass
class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']

admin.site.register(Product,ProductAdminClass)   
admin.site.site_header="Ekart Dashboard"