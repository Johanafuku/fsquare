from django.contrib import admin
from matching.models import MatchResult
# Register your models here.

@admin.register(MatchResult)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        'design',
        'supplier',
        'score',
        'created_at',
                    ]
