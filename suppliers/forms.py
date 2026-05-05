from django import forms
from .models import Supplier, SupplierImage
import ast


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierProfileForm(forms.Form):

    fabric_types = forms.CharField(required=False)
    colors_available = forms.CharField(required=False)
    processing = forms.CharField(required=False)

    min_meters = forms.FloatField(required=False, min_value=0)
    number_of_pieces = forms.IntegerField(required=False, min_value=0)
    contact_email = forms.EmailField(required=False)

    # ---------- PARSER ----------
    def parse_list(self, data):
        if not data:
            return []

        try:
            parsed = ast.literal_eval(data)
            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        except:
            pass

        return [item.strip() for item in data.split(",") if item.strip()]

    def clean(self):
        cleaned = super().clean()

        cleaned["fabric_types"] = self.parse_list(cleaned.get("fabric_types"))
        cleaned["colors_available"] = self.parse_list(cleaned.get("colors_available"))
        cleaned["processing"] = self.parse_list(cleaned.get("processing"))

        return cleaned

class SupplierImageForm(forms.ModelForm):
    class Meta:
        model = SupplierImage
        fields = ["image"]
    

#for the image from suppliers
class SupplierImageForm(forms.ModelForm):
    class Meta:
        model = SupplierImage
        fields = ["image"]