from django.contrib import admin
from designs.models import Design
# Register your models here.

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = [
        'designer',
        'image',
        'fabric_type',
        'color',
        'texture',
        'quantity_meters',
        'created_at',
                    ]