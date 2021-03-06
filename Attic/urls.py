from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='Index'),
    path('Services', views.service, name="Services"),
    path('Consultations', views.consultation, name="Consultations"),
    path('FAQ', views.faq, name="FAQ"),
    path('Reviews', views.reviews, name="Reviews"),
    path('success', views.success, name="Success"),
    path('Register', views.register, name="Register"),
    path('Privacy_Policy', views.privacy, name="Privacy"),
    path('Terms', views.terms, name="Terms"),
]
