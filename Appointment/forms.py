from django import forms
from .models import Consult, FirstFollowUp, SecondFollowUp, ThirdFollowUp, FourthFollowUp, FifthFollowUp, SixthFollowUp


class AppointmentForm(forms.ModelForm):
    consult_date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    consult_time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())

    class Meta:
        model = Consult
        fields = ('consult_date', 'consult_time')


class FirstFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = FirstFollowUp
        fields = ('date', 'time', 'comment')


class SecondFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = SecondFollowUp
        fields = ('date', 'time', 'comment')


class ThirdFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = ThirdFollowUp
        fields = ('date', 'time', 'comment')


class FourthFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = FourthFollowUp
        fields = ('date', 'time', 'comment')


class FifthFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = FifthFollowUp
        fields = ('date', 'time', 'comment')


class SixthFollowUpForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Date', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Additional Comments (Not Required)', max_length=200, required=False,
                              widget=forms.Textarea)

    class Meta:
        model = SixthFollowUp
        fields = ('date', 'time', 'comment')