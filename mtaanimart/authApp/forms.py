from django import forms

class CheckoutForm(forms.Form):
    phone_number = forms.CharField(
        max_length=13,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 2547XXXXXXXX"
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