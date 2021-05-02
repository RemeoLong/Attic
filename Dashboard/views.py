from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from Attic.models import Consultation
from Dashboard.forms import ConsultationUpdateForm, ProfileUpdateForm
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


class ConsultationDetail(ConsultationDetailView):
    template_name = 'index/consult_detail.html'


class ConsultationCreate(ConsultationCreateView):
    template_name = 'index/consult_add.html'


class ConsultationUpdate(ConsultationUpdateView):
    template_name = 'index/consult_update.html'
    success_url = reverse_lazy('Dashboard:ConsultList')
    form_class = ConsultationUpdateForm


class ConsultationDelete(ConsultationDeleteView):
    template_name = 'index/consult_delete.html'
    success_url = reverse_lazy('Dashboard:ConsultList')
    success_message = 'Profile has been successfully Deleted.'


class ConsultationNew(ConsultationList):
    template_name = 'index/consult_new.html'


class ConsultationWorking(ConsultationList):
    template_name = 'index/consult_working.html'


class ConsultationPending(ConsultationList):
    template_name = 'index/consult_pending.html'


class ConsultationConvert(ConsultationList):
    template_name = 'index/consult_convert.html'


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
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('Dashboard:ProfileList')

    def get_object(self, **kwargs):
        return Profile.objects.all()

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(ProfileUpdateView, self).form_valid(form)


class ProfileDelete(ProfileDeleteView):
    template_name = 'index/profile_delete.html'
    success_url = reverse_lazy('Dashboard:ProfileList')


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


class FollowUpOpen(FollowUpList):
    template_name = 'index/appt_open.html'


class FollowUpWorking(FollowUpList):
    template_name = 'index/appt_working.html'


class FollowUpPending(FollowUpList):
    template_name = 'index/appt_pending.html'


class FollowUpComplete(FollowUpList):
    template_name = 'index/appt_complete.html'


