from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['company', 'rent_per_day', 'start_date', 'end_date', 'discount', 'gst', 'due', 'email']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SearchForm(forms.Form):
    invoice_number = forms.IntegerField(label="Invoice Number")
