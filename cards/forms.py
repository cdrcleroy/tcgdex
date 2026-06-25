# forms.py
from django import forms


class CardSearchForm(forms.Form):
    name = forms.CharField(
        label="Nom de la carte",
        max_length=100,
        required=True,
    )
