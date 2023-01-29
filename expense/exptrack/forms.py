from django import forms

from .models import ExpanseTracking


class ExpDesignForm(forms.ModelForm):
    class Meta:
        model = ExpanseTracking
        fields = ["description", "price", "date", "user", "status"]
        widgets = {
            "date": forms.DateInput(
                format="dd-mm-yyyy", attrs={"placeholder": "date", "type": "date"}
            ),
            "price": forms.TextInput(
                attrs={"placeholder": "Amounts", "type": "number"}
            ),
            "description": forms.TextInput(attrs={"placeholder": "Descriptions"}),
            "user": forms.HiddenInput(),
        }
