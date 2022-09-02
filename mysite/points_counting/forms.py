from .models import Transaction, PointsNumber
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['payer_text', 'points', 'date']

        widgets = {
            'payer_text': TextInput(attrs={
                'class': 'form-control',
            }),
            'points': NumberInput(attrs={
                'class': 'form-control',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date',
        })
        }


class PointsNumberForm(ModelForm):
    class Meta:
        model = PointsNumber
        fields = ['number']

        widgets = {
            'number': NumberInput(attrs={
                'class': 'form-control',
            }),
        }