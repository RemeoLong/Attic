from django.shortcuts import render


def index(request):
    return render(request, 'index/home.html', {})


def service(request):
    return render(request, 'index/services.html', {})


def consultation(request):
    return render(request, 'index/consult.html', {})


def faq(request):
    return render(request, 'index/faq.html', {})


def reviews(request):
    return render(request, 'index/reviews.html', {})


