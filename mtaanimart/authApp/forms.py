from django import forms
'''from .models import DeliveryPoint
from leaflet.forms.widgets import LeafletWidget'''


class CheckoutForm(forms.Form):
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. 2547XXXXXXXX',
            'class': 'form-control'
        })
    )

    def clean_phone_number(self):
        number = self.cleaned_data["phone_number"].strip()
        # Enforce international format
        if number.startswith("07"):
            number = "254" + number[1:]
        if not (number.startswith("2547") and number.isdigit() and 12 <= len(number) <= 13):
            raise forms.ValidationError("Use format 2547XXXXXXXX")
        return number



