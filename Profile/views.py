from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProfileForm, EditProfileForm
from .models import Profile


@login_required
def profile(request):
    return render(request, 'index/profile.html', {})


def edit_success(request):
    return render(request, 'index/edit_success.html', {})


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
        id = self.kwargs.get('id')
        return get_object_or_404(Profile, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return get_object_or_404(Profile, id=id)


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
