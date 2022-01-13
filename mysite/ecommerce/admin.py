from django.contrib import admin
from django.http import request
from . import models


admin.site.site_url = '/seller'
admin.site.site_header = 'Administration'
admin.site.site_title = 'Seller'

# Register your models here.
class ElectronicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)

class FashionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)

class HomeDecorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)

class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)


admin.site.register(models.Carousel)
admin.site.register(models.Category)
admin.site.register(models.Seller)
admin.site.register(models.Electronic, ElectronicAdmin)
admin.site.register(models.Fashion, FashionAdmin)
admin.site.register(models.HomeDecor, HomeDecorAdmin)
admin.site.register(models.Mobile, MobileAdmin)