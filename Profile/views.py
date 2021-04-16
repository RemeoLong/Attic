from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProfileForm, EditProfileForm, CreateFollowUpForm
from .models import Profile, FollowUp


@login_required
def profile(request):
    return render(request, 'index/profile.html', {})


def edit_success(request):
    return render(request, 'index/edit_success.html', {})


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
    model = Profile


class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateProfileForm
    queryset = Profile.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'index/edit_profile.html'
    form_class = EditProfileForm

    def get_object(self, **kwargs):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        instance = form.instance
        instance.user = self.request.user
        instance.save()

        return super(ProfileUpdateView, self).form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index/profile_success.html')
            except:
                pass
        else:
            form = CreateProfileForm()
        return render(request, 'index.profile.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index/edit_success.html')
        return render(request, 'index/edit_profile.html', {'profile': profile})

    form = EditProfileForm()
    return render(request, 'index/edit_profile.html', {'form': form})


def show_all_profile(request):
    profile = Profile.objects.all()
    return render(request, 'index/profile_all.html', {'profile': profile})


#def delete_profile(request, id):
#    profile = Profile.objects.get(id=id)
#    profile.delete()
#    return redirect('index/delete_success.html')


class FollowUpCreateView(LoginRequiredMixin, CreateView):
    model = FollowUp
    form_class = CreateFollowUpForm
    template_name = 'index/appointment.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.id = User.objects.get(id=self.request.user)
        return super(FollowUpCreateView, self).form_valid(form)

#    def post(self, request, *args, **kwargs):
#        form = CreateFollowUpForm(data=request.POST, instance=profile)
#        if form.is_valid():
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)

