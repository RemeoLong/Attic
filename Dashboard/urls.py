from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from . import views
from .views import *


app_name = "Dashboard"
urlpatterns = [
    path('home', login_required(views.dash), name='Dashboard'),
    path('profile_list/', login_required(ProfileList.as_view()), name="ProfileList"),
    path('profile_detail/<int:id>/', login_required(ProfileDetail.as_view()), name="ProfileDetails"),
    path('profile_edit/<int:id>/', login_required(ProfileUpdate.as_view()), name="ProfileEdit"),
    path('profile_delete/<int:id>/', login_required(ProfileDelete.as_view()), name="ProfileDelete"),
    path('consult_list/', login_required(ConsultationList.as_view()), name="ConsultList"),
    path('consult_appt', login_required(ConsultationApptList.as_view()), name="ConsultApptList"),
    path('consult_detail/<int:id>/', login_required(ConsultationDetail.as_view()), name="ConsultDetails"),
    path('consult_edit/<int:id>/', login_required(ConsultationUpdate.as_view()), name="ConsultEdit"),
    path('consult_delete/<int:id>/', login_required(ConsultationDelete.as_view()), name="ConsultDelete"),
    path('appt_list/', login_required(FollowUpList.as_view()), name="FollowUpList"),
    path('appt_detail/<int:id>/', login_required(FollowUpDetail.as_view()), name="FollowUpDetails"),
    path('appt_edit/<int:id>/', login_required(FollowUpUpdate.as_view()), name="FollowUpEdit"),
    path('appt_delete/<int:id>/', login_required(FollowUpDelete.as_view()), name="FollowUpDelete"),
    path('base', views.base, name='base'),

]

