from django.contrib import admin
from suppliers.models import Supplier
# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'fabric_types',
        'colors_available',
        'processing',
        'min_meters',
        'contact_email',
                    ]