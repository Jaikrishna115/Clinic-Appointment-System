from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from clinic_.models import Appointment, DoctorProfile, PatientProfile
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator


@login_required
def patient_dashboard(request):
    patient = request.user.patientprofile
    appointments = Appointment.objects.filter(
        patient=patient
    ).order_by("-appointment_date")
    total = appointments.count()
    pending = appointments.filter(status="PENDING").count()
    confirmed = appointments.filter(status="CONFIRMED").count()
    completed = appointments.filter(status="COMPLETED").count()
    context = {
    "appointments": appointments,
    "total": total,
    "pending": pending,
    "confirmed": confirmed,
    "completed": completed,
    }
    return render(request, "dashboard/patient_dashboard.html", context)

@login_required
def cancel_appointment(request,appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        patient=request.user.patientprofile
    )
    if appointment.status == "PENDING":
        appointment.status = "CANCELLED"
        appointment.save()
        messages.success(
            request,
            "Appointment cancelled successfully."
        )
    else:
        messages.error(
            request,
            "Only pending appointments can be cancelled."
        )
    return redirect("dashboard")

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from clinic_.models import Appointment

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from clinic_.models import Appointment

@login_required
def doctor_dashboard(request):

    doctor = request.user.doctorprofile

    appointments = Appointment.objects.select_related(
        "patient__user",
        "doctor__user"
    ).filter(
        doctor=doctor
    )

    # Search & Filters
    search = request.GET.get("search")
    status = request.GET.get("status")
    date = request.GET.get("date")

    if search:
        appointments = appointments.filter(
            patient__user__first_name__icontains=search
        )

    if status:
        appointments = appointments.filter(status=status)

    if date:
        appointments = appointments.filter(
            appointment_date=date
        )

    # Latest appointments first
    appointments = appointments.order_by(
        "-appointment_date",
        "-appointment_time"
    )

    # Counts (Based on Filtered Results)
    total = appointments.count()
    pending = appointments.filter(status="PENDING").count()
    confirmed = appointments.filter(status="CONFIRMED").count()
    completed = appointments.filter(status="COMPLETED").count()

    # Pagination
    paginator = Paginator(appointments, 10)

    page_number = request.GET.get("page")

    appointments = paginator.get_page(page_number)

    context = {
        "appointments": appointments,
        "total": total,
        "pending": pending,
        "confirmed": confirmed,
        "completed": completed,
        "search": search,
        "selected_status": status,
        "selected_date": date,
    }

    return render(
        request,
        "dashboard/doctor_dashboard.html",
        context,
    )
    
@staff_member_required
def admin_dashboard(request):
    doctors = DoctorProfile.objects.count()
    patients = PatientProfile.objects.count()
    appointments = Appointment.objects.count()
    pending = Appointment.objects.filter(status="PENDING").count()
    recent_appointments = Appointment.objects.select_related(
        "patient__user",
        "doctor__user"
    ).order_by("-created_at")[:10]
    context = {
        "doctors": doctors,
        "patients": patients,
        "appointments": appointments,
        "pending": pending,
        "recent_appointments": recent_appointments,
    }
    return render(request, "dashboard/admin_dashboard.html", context)