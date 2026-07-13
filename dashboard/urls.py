from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_dashboard, name="dashboard"),
    path("cancel/<int:appointment_id>/",views.cancel_appointment,name="cancel_appointments",),
    path("doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("admin-dashboard/",views.admin_dashboard, name="admin_dashboard"),
]