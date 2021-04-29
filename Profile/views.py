from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import CreateProfileForm, EditProfileForm, CreateFollowUpForm, EditFollowUpForm
from .models import Profile, FollowUp


def add_services(request):
    return render(request, 'index/add_service.html', {})


def profile_home(request):
    return render(request, 'index/profile_home.html', {})


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)

        return queryset


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'index/profile_home.html'

    def get_object(self, **kwargs):
        return Profile.objects.get(user=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'index/edit_profile.html'
    form_class = EditProfileForm
    success_message = 'Profile has been successfully Updated'

    def get_object(self, **kwargs):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(ProfileUpdateView, self).form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    success_message = 'Profile has been successfully Deleted.'

    def get_object(self, **kwargs):
        return Profile.objects.get(user=self.request.user)


class FollowUpListView(LoginRequiredMixin, ListView):
    model = FollowUp
    template_name = 'index/appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
#        context['total_open_followup'] = self.queryset.filter(Status='Open').count()
        return context

    def get_queryset(self, **kwargs):
        return FollowUp.objects.filter(user=self.request.user)


class FollowUpDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'index/appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_object(self, **kwargs):
        return FollowUp.objects.filter(user=self.request.user)


class FollowUpCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = FollowUp
    form_class = CreateFollowUpForm
    template_name = 'index/book_appointment.html'
    success_message = 'Your Appointment has been Booked.'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(FollowUpCreateView, self).form_valid(form)


class FollowUpUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FollowUp
    form_class = EditFollowUpForm
    template_name = 'index/edit_appointment.html'
    success_message = 'Your Appointment has been Updated.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(FollowUpUpdateView, self).form_valid(form)


class FollowUpDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FollowUp
    template_name = 'index/appt_confirm_delete.html'
    success_message = 'Your Appointment has been Deleted.'
    success_url = reverse_lazy('Profile:Appointment')

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(FollowUpDeleteView, self).form_valid(form)
