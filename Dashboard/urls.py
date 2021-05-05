from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from . import views
from .views import *


app_name = "Dashboard"
urlpatterns = [
    path('home', staff_member_required(Dashboard.as_view()), name='Dashboard'),
    path('profile_list/', staff_member_required(ProfileList.as_view()), name="ProfileList"),
    path('profile_detail/<int:id>/', staff_member_required(ProfileDetail.as_view()), name="ProfileDetails"),
    path('profile_create', staff_member_required(ProfileCreate.as_view()), name="ProfileCreate"),
    path('profile_edit/<int:pk>/', staff_member_required(ProfileUpdate.as_view()), name="ProfileEdit"),
    path('profile_delete/<int:pk>/', staff_member_required(ProfileDelete.as_view()), name="ProfileDelete"),

    path('consult_list/', staff_member_required(ConsultationList.as_view()), name="ConsultList"),
    path('consult_appt', staff_member_required(ConsultationApptList.as_view()), name="ConsultApptList"),
    path('consult_app_edit/<int:pk>/', staff_member_required(ConsultationApptUpdate.as_view()), name='ConsultationApptUpdate'),
    path('consult_detail/<int:id>/', staff_member_required(ConsultationDetail.as_view()), name="ConsultDetails"),
    path('consult_create', staff_member_required(ConsultationCreate.as_view()), name="ConsultCreate"),
    path('consult_edit/<int:pk>/', staff_member_required(ConsultationUpdate.as_view()), name="ConsultEdit"),
    path('consult_delete/<int:pk>/', staff_member_required(ConsultationDelete.as_view()), name="ConsultDelete"),
    path('consult_new', staff_member_required(ConsultationNew.as_view()), name="ConsultNewList"),
    path('consult_working', staff_member_required(ConsultationWorking.as_view()), name="ConsultWorkingList"),
    path('consult_pending', staff_member_required(ConsultationPending.as_view()), name="ConsultPendingList"),
    path('consult_convert', staff_member_required(ConsultationConvert.as_view()), name="ConsultCustomerList"),

    path('appt_list/', staff_member_required(FollowUpList.as_view()), name="FollowUpList"),
    path('appt_detail/<int:id>/', staff_member_required(FollowUpDetail.as_view()), name="FollowUpDetails"),
    path('appt_create', staff_member_required(FollowUpCreate.as_view()), name="FollowUpCreate"),
    path('appt_edit/<int:pk>/', staff_member_required(FollowUpUpdate.as_view()), name="FollowUpEdit"),
    path('appt_delete/<int:pk>/', staff_member_required(FollowUpDelete.as_view()), name="FollowUpDelete"),
    path('appt_open', staff_member_required(FollowUpOpen.as_view()), name="FollowUpOpenList"),
    path('appt_working', staff_member_required(FollowUpWorking.as_view()), name="FollowUpWorkingList"),
    path('appt_pending', staff_member_required(FollowUpPending.as_view()), name="FollowUpPendingList"),
    path('appt_complete', staff_member_required(FollowUpComplete.as_view()), name="FollowUpCompleteList"),

]

