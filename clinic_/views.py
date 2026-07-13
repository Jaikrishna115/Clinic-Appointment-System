from django.shortcuts import render, redirect, get_object_or_404
from .models import PatientProfile, DoctorProfile, Appointment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm, DoctorForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def home(request):
    return render(request, "clinic_/home.html")

@login_required
def book_appointment(request):
    if request.method =="POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patientprofile
            appointment.save()
            messages.success(request,"Appointment booked successfully.")
            return redirect("home")
    else:
        form = AppointmentForm()
    return render(request,"clinic_/book_appointment.html",{"form":form})

@login_required
def confirm_appointment(request, appointment_id):
    doctor = request.user.doctorprofile
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )
    if appointment.status == "PENDING":
        appointment.status = "CONFIRMED"
        appointment.save()
        messages.success(request, "Appointment confirmed successfully.")
    else:
        messages.error(request, "Only pending appointments can be confirmed.")
    return redirect("doctor_dashboard")

@login_required
def complete_appointment(request, appointment_id):
    doctor = request.user.doctorprofile
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )
    if appointment.status == "CONFIRMED":
        appointment.status = "COMPLETED"
        appointment.save()
        messages.success(request, "Appointment marked as completed.")
    else:
        messages.error(request, "Only confirmed appointments can be completed.")
    return redirect("doctor_dashboard")

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        patient=request.user.patientprofile
    )
    if appointment.status == "PENDING":
        appointment.status = "CANCELLED"
        appointment.save()
        messages.success(request, "Appointment cancelled successfully.")
    else:
        messages.error(request, "Only pending appointments can be cancelled.")
    return redirect("dashboard")

@staff_member_required
def doctor_list(request):
    doctors = DoctorProfile.objects.select_related("user")
    return render(
        request,
        "clinic_/doctor_list.html",
        {
            "doctors": doctors
        }
    )
    
@login_required
def profile(request):
    # Admin
    if request.user.is_staff:
        messages.info(request, "Admin profile is managed through the Admin Dashboard.")
        return redirect("admin_dashboard")
    # Patient
    if hasattr(request.user, "patientprofile"):
        patient = request.user.patientprofile
        # Your existing patient profile update logic goes here
    # Doctor
    elif hasattr(request.user, "doctorprofile"):
        doctor = request.user.doctorprofile
        # We'll build the doctor profile update next
    else:
        messages.error(request, "Profile not found.")
        return redirect("home")