from django import forms
from .models import Appointment, FollowUps


class AppointmentForm(forms.ModelForm):
    consult_date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    consult_time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput())

    class Meta:
        model = Appointment
        fields = ('consult_date', 'consult_time')


class CreateAppointmentForm(forms.ModelForm):
    consult = forms.CharField()
    consult_date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    consult_time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput())

    class Meta:
        model = Appointment
        fields = ('consult', 'consult_date', 'consult_time')


class EditAppointmentForm(forms.ModelForm):
    consult_date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    consult_time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput())

    class Meta:
        model = Appointment
        fields = ('consult_date', 'consult_time')


class CreateFollowUpForm(forms.ModelForm):
    profile = forms.CharField()
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Comments', max_length=500, required=False,
                              widget=forms.Textarea)
    status = forms.CharField()

    class Meta:
        model = FollowUps
        fields = ('profile', 'date', 'time', 'comment', 'status')


class EditFollowUpsForm(forms.ModelForm):
    date = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput())
    comment = forms.CharField(label='Comments', max_length=500, required=False,
                              widget=forms.Textarea)
    status = forms.CharField()

    class Meta:
        model = FollowUps
        fields = ('date', 'time', 'comment', 'status')
