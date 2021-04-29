from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ConsultForm
from .models import Consultation


def index(request):
    return render(request, 'index/home.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Profile/home')
    else:
        form = UserCreationForm()
    return render(request, 'index/register.html', {'form': form})


def service(request):
    return render(request, 'index/services.html', {})


def success(request):
    return render(request, 'index/success.html', {})


def faq(request):
    return render(request, 'index/faq.html', {})


def reviews(request):
    return render(request, 'index/reviews.html', {})


def consultation(request):
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
            }
            date = {'consult_date': form.cleaned_data['consult_date']}
            time = {'consult_time': form.cleaned_data['consult_time']}
            message = "\n".join(body.values()) + str(date) + str(time)
            form.save()

            try:
                send_mail(subject, message, 'admin@atticrestorations.biz', ['admin@atticrestorations.biz'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Success')

    form = ConsultForm()
    return render(request, "index/consult.html", {'form': form})


class ConsultationListView(LoginRequiredMixin, ListView):
    model = Consultation


class ConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Consultation


class ConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Consultation
    fields = ['user', 'email', 'first_name', 'last_name', 'service_address', 'city', 'state', 'zip_code',
              'phone_number', 'services', 'consult_date', 'consult_time', 'comment']


class ConsultationUpdateView(LoginRequiredMixin, UpdateView):
    model = Consultation
    fields = ['consult_date', 'consult_time']


class ConsultationDeleteView(LoginRequiredMixin, DeleteView):
    model = Consultation








