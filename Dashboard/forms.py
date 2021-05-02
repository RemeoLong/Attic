from django import forms

from Attic.models import Consultation
from Attic.forms import DateInput, TimeInput
from Profile.models import Profile


class ConsultationUpdateForm(forms.ModelForm):
    email = forms.CharField(label='Email Address', max_length=100, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label='First Name', max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(label='Contact Number', max_length=15, required=False,
                                   widget=forms.TextInput(attrs={'class': "form-control"}))
    service_address = forms.CharField(label='Service Address', max_length=100, required=False,
                                      widget=forms.TextInput(attrs={'class': "form-control"}))
    city = forms.CharField(label='City', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    state = forms.CharField(label='State', max_length=25, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    zip_code = forms.CharField(label='Zip Code', max_length=12, required=False,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    consult_date = forms.DateField(widget=DateInput, required=False)
    consult_time = forms.TimeField(widget=TimeInput, required=False)
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=500, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = Consultation
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'service', 'service_address', 'city', 'state',
                  'zip_code', 'consult_date', 'consult_time', 'comment', 'status')


class ProfileUpdateForm(forms.ModelForm):
    email = forms.CharField(label='Email Address', max_length=100, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label='First Name', max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    service_address = forms.CharField(label='Service Address', max_length=100, required=False,
                                      widget=forms.TextInput(attrs={'class': "form-control"}))
    city = forms.CharField(label='City', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    state = forms.CharField(label='State', max_length=25, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    zip_code = forms.CharField(label='Zip Code', max_length=12, required=False,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(label='Contact Number', max_length=15, required=False,
                                   widget=forms.TextInput(attrs={'class': "form-control"}))
    warranty_start_date = forms.DateField(widget=DateInput, required=False)
    warranty_end_date = forms.DateField(widget=DateInput, required=False)

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'service_address', 'city', 'state', 'zip_code', 'phone_number',
                  'services', 'additional_service', 'warranty_start_date', 'warranty_end_date', 'warranty', 'invoice')
