from django import forms

from Attic.forms import TimeInput, DateInput
from .models import Profile, FollowUp


class EditProfileForm(forms.ModelForm):
    email = forms.CharField(label='Email Address', max_length=100, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(label='First Name', max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(label='Contact Number', max_length=15, required=False,
                                   widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'phone_number')


class CreateProfileForm(forms.ModelForm):
    user = forms.CharField()
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    service_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    state = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control"}))
    zip_code = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': "form-control"}))
    services = ()

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'phone_number')


class CreateFollowUpForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    comment = forms.CharField(label='Comments', max_length=500, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = FollowUp
        fields = ('date', 'time', 'comment')


class EditFollowUpForm(forms.ModelForm):
    date = forms.DateField(required=True, widget=DateInput)
    time = forms.TimeField(required=True, widget=TimeInput())
    comment = forms.CharField(label='Comments', max_length=500, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = FollowUp
        fields = ('date', 'time', 'comment')
