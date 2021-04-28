from django.shortcuts import render
from django.views.generic import ListView

from Profile.models import Profile, FollowUp
from Profile.views import ProfileListView, FollowUpListView, ProfileDetailView, FollowUpDetailView, ProfileUpdateView, \
    ProfileDeleteView, FollowUpUpdateView, FollowUpDeleteView


def dash(request):
    return render(request, 'index/index.html', {})


class ProfileList(ProfileListView):
    template_name = 'index/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileDetail(ProfileDetailView):
    template_name = 'index/profile_detail.html'


class ProfileUpdate(ProfileUpdateView):
    template_name = 'index/profile_update.html'


class ProfileDelete(ProfileDeleteView):
    template_name = 'index/profile_delete.html'


class FollowUpList(FollowUpListView):
    template_name = 'index/appt_list.html'

    def get_object(self, **kwargs):
        return FollowUp.objects.get.all(user=self.request.user)


class FollowUpDetail(FollowUpDetailView):
    template_name = 'index/appt_detail.html'


class FollowUpUpdate(FollowUpUpdateView):
    template_name = 'index/appt_update.html'


class FollowUpDelete(FollowUpDeleteView):
    template_name = 'index/appt_delete.html'

