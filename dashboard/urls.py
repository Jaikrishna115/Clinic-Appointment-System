from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_dashboard, name="patient_dashboard"),

    path(
        "confirm/<int:appointment_id>/",
        views.confirm_appointment,
        name="confirm_appointment",
    ),

    path(
        "complete/<int:appointment_id>/",
        views.complete_appointment,
        name="complete_appointment",
    ),

    path(
        "admin-cancel/<int:appointment_id>/",
        views.cancel_appointment_admin,
        name="cancel_appointment_admin",
    ),

    path(
        "doctor/",
        views.doctor_dashboard,
        name="doctor_dashboard",
    ),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard",
    ),
]