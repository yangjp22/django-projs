from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstName', 'lastName', 'email', 'address', 'postalCode', 'city']
        labels = {
            'firstName': 'First name',
            'lastName': 'Last name',
            'postalCode': 'Postal code',
        }