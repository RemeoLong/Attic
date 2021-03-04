from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConsultForm


def index(request):
    return render(request, 'index/home.html', {})


def service(request):
    return render(request, 'index/services.html', {})


def consultation(request):
    if request.method == "POST":
        c_form = ConsultForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Your Consultation request has been submitted. Please check your email")
            return redirect('Consultations')
        else:
            messages.error(request, "Please correct the following errors: ")
    else:
        c_form = ConsultForm
    return render(request, 'index/consult.html', {'c_form': c_form})


def faq(request):
    return render(request, 'index/faq.html', {})


def reviews(request):
    return render(request, 'index/reviews.html', {})


