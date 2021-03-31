from django import forms
from .models import *


class ConsultForm(forms.ModelForm):
    email = forms.CharField(label='Email Address', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label='First Name', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(label='Contact Number', max_length=15, required=True,
                                   widget=forms.TextInput(attrs={'class': "form-control"}))
    service_address = forms.CharField(label='Service Address', max_length=100, required=True,
                                      widget=forms.TextInput(attrs={'class': "form-control"}))
    city = forms.CharField(label='City', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    state = forms.CharField(label='State', max_length=25, required=True,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    zip_code = forms.CharField(label='Zip Code', max_length=12, required=True,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=500, required=False,
                              widget=forms.Textarea)
    consult_date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    consult_time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())

    class Meta:
        model = Consultation
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'service', 'service_address', 'city', 'state',
                  'zip_code', 'comment')
