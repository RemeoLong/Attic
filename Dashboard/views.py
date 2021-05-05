from datetime import date, datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
#from django.views.generic.base import View

from Attic.models import Consultation
from Dashboard.forms import ConsultationUpdateForm, ProfileUpdateForm, CreateFollowUp, EditFollowUp, \
    ConsultApptUpdateForm
from Profile.forms import EditFollowUpForm
from Profile.models import Profile, FollowUp
from Attic.views import ConsultationListView, ConsultationDetailView, ConsultationCreateView, ConsultationUpdateView, \
    ConsultationDeleteView
from Profile.views import ProfileListView, FollowUpListView, ProfileDetailView, FollowUpDetailView, ProfileUpdateView, \
    ProfileDeleteView, FollowUpUpdateView, FollowUpDeleteView, FollowUpCreateView


def dash(request):
    return render(request, 'index/dashboard.html', {})


class Dashboard(ListView):
    template_name = 'index/dashboard.html'
    queryset = Consultation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appt'] = FollowUp.objects.all()
        context['appt_today'] = FollowUp.objects.filter()
        context['consult_count'] = Consultation.objects.filter().count()
        context['consult_new_count'] = Consultation.objects.filter(status="New").count()
        context['consult_working_count'] = Consultation.objects.filter(status="Working").count()
        context['consult_pending_count'] = Consultation.objects.filter(status="Pending Customer").count()
        context['consult_convert_count'] = Consultation.objects.filter(status="Customer").count()
        context['consult_today'] = Consultation.objects.filter(consult_date=datetime.now())
        context['cust_count'] = Profile.objects.filter().count()
        context['followup_open_count'] = FollowUp.objects.filter(status="Open").count()
        context['followup_working_count'] = FollowUp.objects.filter(status="Working").count()
        context['followup_pending_count'] = FollowUp.objects.filter(status="Pending").count()
        context['followup_complete_count'] = FollowUp.objects.filter(status="Complete").count()
        context['followup_today'] = FollowUp.objects.filter(date=datetime.now())
        return context


class ConsultationList(ConsultationListView, Dashboard):
    template_name = 'index/consult_list.html'

    def get_queryset(self, **kwargs):
        return Consultation.objects.all()


class ConsultationApptList(ConsultationList, Dashboard):
    template_name = 'index/consult_appt_list.html'


class ConsultationApptUpdate(ConsultationUpdateView, Dashboard):
    template_name = 'index/consult_appt_update.html'
    success_url = reverse_lazy('Dashboard:ConsultApptList')
    form_class = ConsultApptUpdateForm


class ConsultationDetail(ConsultationDetailView, Dashboard):
    template_name = 'index/consult_detail.html'


class ConsultationCreate(ConsultationCreateView, Dashboard):
    template_name = 'index/consult_add.html'
    success_url = reverse_lazy('Dashboard:ConsultList')


class ConsultationUpdate(ConsultationUpdateView, Dashboard):
    template_name = 'index/consult_update.html'
    success_url = reverse_lazy('Dashboard:ConsultList')
    form_class = ConsultationUpdateForm


class ConsultationDelete(ConsultationDeleteView):
    template_name = 'index/consult_delete.html'
    success_url = reverse_lazy('Dashboard:ConsultList')
    success_message = 'Profile has been successfully Deleted.'


class ConsultationNew(ConsultationList, Dashboard):
    template_name = 'index/consult_new.html'


class ConsultationWorking(ConsultationList, Dashboard):
    template_name = 'index/consult_working.html'


class ConsultationPending(ConsultationList, Dashboard):
    template_name = 'index/consult_pending.html'


class ConsultationConvert(ConsultationList, Dashboard):
    template_name = 'index/consult_convert.html'


class ProfileList(Dashboard, ProfileListView):
    template_name = 'index/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        return Profile.objects.all()


class ProfileDetail(ProfileDetailView, Dashboard):
    template_name = 'index/profile_detail.html'


class ProfileCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView, Dashboard):
    model = Profile
    template_name = 'index/profile_add.html'
    success_url = reverse_lazy('Dashboard:ProfileList')
    form_class = UserCreationForm


class ProfileUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView, Dashboard):
    model = Profile
    template_name = 'index/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('Dashboard:ProfileList')
    success_message = 'Profile has been successfully Updated'
    queryset = Profile.objects.all()


class ProfileDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Profile
    template_name = 'index/profile_delete.html'
    success_url = reverse_lazy('Dashboard:ProfileList')
    success_message = 'Profile has been successfully Deleted'


class FollowUpList(Dashboard, FollowUpListView):
    template_name = 'index/appt_list.html'

    def get_queryset(self, **kwargs):
        return FollowUp.objects.all()


class FollowUpDetail(FollowUpDetailView):
    template_name = 'index/appt_detail.html'


class FollowUpCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView, Dashboard):
    template_name = 'index/appt_add.html'
    form_class = CreateFollowUp
    success_url = reverse_lazy('Dashboard:FollowUpList')


class FollowUpUpdate(FollowUpUpdateView, Dashboard):
    template_name = 'index/appt_update.html'
    form_class = EditFollowUp
    success_url = reverse_lazy('Dashboard:FollowUpList')
    queryset = FollowUp.objects.all()


class FollowUpDelete(FollowUpDeleteView):
    template_name = 'index/appt_delete.html'
    success_url = reverse_lazy('Dashboard:FollowUpList')


class FollowUpOpen(FollowUpList):
    template_name = 'index/appt_open.html'


class FollowUpWorking(FollowUpList):
    template_name = 'index/appt_working.html'


class FollowUpPending(FollowUpList):
    template_name = 'index/appt_pending.html'


class FollowUpComplete(FollowUpList):
    template_name = 'index/appt_complete.html'


