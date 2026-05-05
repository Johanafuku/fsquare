from django.contrib import admin
from suppliers.models import Supplier, SupplierImage
# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'fabric_types',
        'colors_available',
        'processing',
        'min_meters',
        'number_of_pieces',
        'contact_email',
                    ]
    
admin.site.register(SupplierImage)