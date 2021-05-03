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
    path('profile_create', login_required(ProfileCreate.as_view()), name="ProfileCreate"),
    path('profile_edit/<int:pk>/', login_required(ProfileUpdate.as_view()), name="ProfileEdit"),
    path('profile_delete/<int:pk>/', login_required(ProfileDelete.as_view()), name="ProfileDelete"),

    path('consult_list/', login_required(ConsultationList.as_view()), name="ConsultList"),
    path('consult_appt', login_required(ConsultationApptList.as_view()), name="ConsultApptList"),
    path('consult_app_edit/<int:pk>/', login_required(ConsultationApptUpdate.as_view()), name='ConsultationApptUpdate'),
    path('consult_detail/<int:id>/', login_required(ConsultationDetail.as_view()), name="ConsultDetails"),
    path('consult_create', login_required(ConsultationCreate.as_view()), name="ConsultCreate"),
    path('consult_edit/<int:pk>/', login_required(ConsultationUpdate.as_view()), name="ConsultEdit"),
    path('consult_delete/<int:pk>/', login_required(ConsultationDelete.as_view()), name="ConsultDelete"),
    path('consult_new', login_required(ConsultationNew.as_view()), name="ConsultNewList"),
    path('consult_working', login_required(ConsultationWorking.as_view()), name="ConsultWorkingList"),
    path('consult_pending', login_required(ConsultationPending.as_view()), name="ConsultPendingList"),
    path('consult_convert', login_required(ConsultationConvert.as_view()), name="ConsultCustomerList"),

    path('appt_list/', login_required(FollowUpList.as_view()), name="FollowUpList"),
    path('appt_detail/<int:id>/', login_required(FollowUpDetail.as_view()), name="FollowUpDetails"),
    path('appt_create', login_required(FollowUpCreate.as_view()), name="FollowUpCreate"),
    path('appt_edit/<int:pk>/', login_required(FollowUpUpdate.as_view()), name="FollowUpEdit"),
    path('appt_delete/<int:pk>/', login_required(FollowUpDelete.as_view()), name="FollowUpDelete"),
    path('appt_open', login_required(FollowUpOpen.as_view()), name="FollowUpOpenList"),
    path('appt_working', login_required(FollowUpWorking.as_view()), name="FollowUpWorkingList"),
    path('appt_pending', login_required(FollowUpPending.as_view()), name="FollowUpPendingList"),
    path('appt_complete', login_required(FollowUpComplete.as_view()), name="FollowUpCompleteList"),

]

