from django.urls import path
from . import views
from .cbv_views import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path("", views.home, name="home"),
    path("book/",views.book_appointment, name="book_appointment"),
    path("cancel/<int:appointment_id>/", views.cancel_appointment, name="cancel_appointment"),
    path("confirm/<int:appointment_id>/", views.confirm_appointment, name="confirm_appointment"),
    path("complete/<int:appointment_id>/", views.complete_appointment, name="complete_appointment"),
    path("doctors/",DoctorListView.as_view(), name="doctor_list",),
    path("doctors/add/",DoctorCreateView.as_view(), name="add_doctor",),
    path("doctors/edit/<int:of>/",DoctorUpdateView.as_view(),name="edit_doctor",),
    path("doctors/delete/<int:pk>/",DoctorDeleteView.as_view(),name="delete_doctor",),
]
