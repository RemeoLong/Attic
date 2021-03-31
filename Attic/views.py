from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConsultForm


def index(request):
    return render(request, 'index/home.html', {})


def service(request):
    return render(request, 'index/services.html', {})


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


def success(request):
    return render(request, 'index/success.html', {})


def faq(request):
    return render(request, 'index/faq.html', {})


def reviews(request):
    return render(request, 'index/reviews.html', {})