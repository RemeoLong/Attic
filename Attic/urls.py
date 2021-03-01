from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('Services', views.service, name="Services"),
    path('Consultations', views.consultation, name="Consultations"),
    path('FAQ', views.faq, name="FAQ"),
    path('Reviews', views.reviews, name="Reviews"),
]