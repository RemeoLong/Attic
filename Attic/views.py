from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .forms import ConsultForm, EditProfileForm, CreateProfileForm
from .models import Profile


def index(request):
    return render(request, 'index/home.html', {})


def service(request):
    return render(request, 'index/services.html', {})


def success(request):
    return render(request, 'index/success.html', {})


def edit_success(request):
    return render(request, 'index/edit_success.html', {})


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
            message = "\n".join(body.values())
            form.save()

            try:
                send_mail(subject, message, 'admin@atticrestorations.biz', ['admin@atticrestorations.biz'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Success')

    form = ConsultForm()
    return render(request, "index/consult.html", {'form': form})


#def ProfileListView(ListView):

#def ProfileDetailView(DetailView):


@login_required
def profile(request):
    return render(request, 'index/profile.html', {})


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


def delete_profile(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('index/delete_success.html')



