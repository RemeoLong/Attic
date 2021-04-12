from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.views.generic import ListView, DetailView

from Attic.forms import ConsultForm
from Attic.models import Consultation
from .models import Appointment


class AppointmentView(ListView):
    template_name = 'index/consult.html'
    context_object_name = 'consult_list'

    def get_queryset(self):
        return Appointment.objects.all()


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'index/profile.html'

    def create(request):
        if request.method == "POST":
            form = ConsultForm(request.POST)
            if form.is_valid():
                subject = "Consultations Request"
                body = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'phone': form.cleaned_data['phone_number'],
                    'services': form.cleaned_data['service'],
                    'address': form.cleaned_data['service_address'],
                    'city': form.cleaned_data['city'],
                    'zipcode': form.cleaned_data['zip_code'],
                    'comment': form.cleaned_data['comment'],
                    'consult_date': form.cleaned_data['consult_date'],
                    'consult_time': form.cleaned_data['consult_time'],
            }
            message = "\n".join(body.values())
            form.save()

            try:
                send_mail(subject, message, 'admin@atticrestorations.biz', ['admin@atticrestorations.biz'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Success')

        form = ConsultForm()
        return render(request, "index/consult.html", {'form': form})

    def edit(request, pk, template_name='index/edit.html'):
        consult = get_object_or_404(Consultation, pk=pk)
        form = ConsultForm(request.POST or None, instance=Post)
        if form.is_valid():
            form.save()
            return redirect('index/success.html')
        return render(request, template_name, {'form':form})

    def delete(request, pk, template_name='index/delete.html'):
        consult = get_object_or_404(Consultation, pk=pk)
        if request.method == 'POST':
            consult.delete()
            return redirect('index/delete.html')
        return render(request, template_name='index/success.html')


class AppointmentListView(ListView):
    model= Appointment


class AppoointmentDetailView(DetailView):
    model = Appointment



#class Appointment(request):

    def show_all_appt(request):
        appt = Appointment.objects.all()
        return render(request, 'index/appointment.html', {'appt': appt})

    def create_appt(request):
        if request.method == "POST":
            form = CreateAppointment(request.POST, instance=Appointment)
            if form.is_valid():
                form.save()
                return redirect('index/Appt_success.html')
            return render(request, 'index/consult.html', {'form': form})

    def edit_appt(request):
        if request.method == "POST":
            form = EditAppointment(request.POST, instance=Appointment)
            if form.is_valid():
                form.save()
                return render(request, 'index/Appt_success.html')
            return render(request, 'index/edit_appt.html', {'form': form})

    def delete_appt(request, id):
        appt = Appointment.objects.get(id=id)
        Appointment.delete()
        return redirect('index/appointment.html')








