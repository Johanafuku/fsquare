from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierProfileForm(forms.ModelForm):

    fabric_types = forms.CharField(required=False)
    colors_available = forms.CharField(required=False)
    processing = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'woven, non woven'}))
    min_meters = forms.FloatField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder':'e.g. 100'}))
    contact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder':'example@email.com'}))


    class Meta:
        model = Supplier
        fields = [
            'fabric_types',
            'colors_available',
            'processing',
            'min_meters',
            'contact_email'
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.fabric_types:
            self.fields['fabric_types'].initial = ', '.join(self.instance.fabric_types)

        if self.instance.colors_available:
            self.fields['colors_available'].initial = ', '.join(self.instance.colors_available)

        if self.instance.processing:
            self.fields['processing'].initial = ', '.join(self.instance.processing)

    # Convert text → list
    def clean_fabric_types(self):
        data = self.cleaned_data.get('fabric_types', '')
        return [item.strip() for item in data.split(',') if item.strip()]

    def clean_colors_available(self):
        data = self.cleaned_data.get('colors_available', '')
        return [item.strip() for item in data.split(',') if item.strip()]

    def clean_processing(self):
        data = self.cleaned_data.get('processing', '')
        return [item.strip() for item in data.split(',') if item.strip()]

    # Extra validation (optional but good)
    def clean_min_meters(self):
        value = self.cleaned_data.get('min_meters')

        if value is not None and value < 0:
            raise forms.ValidationError("Minimum meters must be positive")

        return value