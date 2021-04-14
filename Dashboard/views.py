from django.views.generic import ListView

from Profile.models import Profile


class ProfileListView(ListView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
