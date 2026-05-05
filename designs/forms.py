from django import forms
from .models import Design

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = [
            'image',
            'fabric_type',
            'color',
            'texture',
            'quantity_meters',
            'pieces'
        ]
