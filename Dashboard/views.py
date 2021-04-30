from django.shortcuts import render
from django.views.generic import ListView

from Attic.models import Consultation
from Profile.models import Profile, FollowUp
from Attic.views import ConsultationListView, ConsultationDetailView, ConsultationCreateView, ConsultationUpdateView, \
    ConsultationDeleteView
from Profile.views import ProfileListView, FollowUpListView, ProfileDetailView, FollowUpDetailView, ProfileUpdateView, \
    ProfileDeleteView, FollowUpUpdateView, FollowUpDeleteView, FollowUpCreateView


def dash(request):
    return render(request, 'index/dashboard.html', {})


class ConsultationList(ConsultationListView):
    template_name = 'index/consult_list.html'

    def get_queryset(self, **kwargs):
        return Consultation.objects.all()


class ConsultationApptList(ConsultationList):
    template_name = 'index/consult_appt_list.html'

    def get_queryset(self, **kwargs):
        return Consultation.objects.all()


class ConsultationDetail(ConsultationDetailView):
    template_name = 'index/consult_detail.html'


class ConsultationCreate(ConsultationCreateView):
    template_name = 'index/consult_add.html'


class ConsultationUpdate(ConsultationUpdateView):
    template_name = 'index/consult_update.html'


class ConsultationDelete(ConsultationDeleteView):
    template_name = 'index/consult_delete.html'


class ProfileList(ProfileListView):
    template_name = 'index/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        return Profile.objects.all()


class ProfileDetail(ProfileDetailView):
    template_name = 'index/profile_detail.html'


class ProfileUpdate(ProfileUpdateView):
    template_name = 'index/profile_update.html'


class ProfileDelete(ProfileDeleteView):
    template_name = 'index/profile_delete.html'


class FollowUpList(FollowUpListView):
    template_name = 'index/appt_list.html'

    def get_queryset(self, **kwargs):
        return FollowUp.objects.all()


class FollowUpDetail(FollowUpDetailView):
    template_name = 'index/appt_detail.html'


class FollowUpCreate(FollowUpCreateView):
    template_name = 'index/appt_add.html'


class FollowUpUpdate(FollowUpUpdateView):
    template_name = 'index/appt_update.html'


class FollowUpDelete(FollowUpDeleteView):
    template_name = 'index/appt_delete.html'

