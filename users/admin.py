from django.contrib import admin

# Register your models here.
from users.models import Designer

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['user','brand_name','email','bio','profile_picture']