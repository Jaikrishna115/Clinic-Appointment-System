from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from clinic_.models import Appointment, DoctorProfile, PatientProfile
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from datetime import date
from django.db.models import Q,Sum


from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def patient_dashboard(request):

    patient = request.user.patientprofile

    appointments = Appointment.objects.select_related(
        "doctor__user"
    ).filter(
        patient=patient
    )

    search = request.GET.get("search")
    status = request.GET.get("status")
    selected_date = request.GET.get("date")

    if search:
        appointments = appointments.filter(
            Q(doctor__user__first_name__icontains=search) |
            Q(doctor__user__last_name__icontains=search)
        )

    if status:
        appointments = appointments.filter(status=status)

    if selected_date:
        appointments = appointments.filter(
            appointment_date=selected_date
        )

    appointments = appointments.order_by(
        "-appointment_date",
        "-appointment_time"
    )

    context = {
        "appointments": appointments,
        "total": appointments.count(),
        "pending": appointments.filter(status="PENDING").count(),
        "confirmed": appointments.filter(status="CONFIRMED").count(),
        "completed": appointments.filter(status="COMPLETED").count(),
        "search": search,
        "selected_status": status,
        "selected_date": selected_date,
    }

    return render(
        request,
        "dashboard/patient_dashboard.html",
        context,
    )
    
@staff_member_required
def complete_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    appointment.status = "COMPLETED"
    appointment.save()

    messages.success(
        request,
        "Appointment completed."
    )

    return redirect("admin_dashboard")

@staff_member_required
def cancel_appointment_admin(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    appointment.status = "CANCELLED"
    appointment.save()

    messages.success(
        request,
        "Appointment cancelled."
    )

    return redirect("admin_dashboard")

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
    
@login_required
def admin_dashboard(request):

    # Dashboard Statistics
    total_patients = PatientProfile.objects.count()
    total_doctors = DoctorProfile.objects.count()
    total_appointments = Appointment.objects.count()

    pending = Appointment.objects.filter(status="PENDING").count()
    confirmed = Appointment.objects.filter(status="CONFIRMED").count()
    completed = Appointment.objects.filter(status="COMPLETED").count()
    cancelled = Appointment.objects.filter(status="CANCELLED").count()

    available_doctors = DoctorProfile.objects.filter(
        is_available=True
    ).count()

    unavailable_doctors = DoctorProfile.objects.filter(
        is_available=False
    ).count()

    today_appointments = Appointment.objects.filter(
        appointment_date=date.today()
    ).count()

    # Search & Filter Inputs
    search = request.GET.get("search")
    status = request.GET.get("status")
    selected_date = request.GET.get("date")

    # Recent Appointments
    recent_appointments = Appointment.objects.select_related(
        "patient__user",
        "doctor__user",
    )

    # Search by Patient or Doctor Name
    if search:
        recent_appointments = recent_appointments.filter(
            Q(patient__user__username__icontains=search) |
            Q(patient__user__first_name__icontains=search) |
            Q(patient__user__last_name__icontains=search) |
            Q(doctor__user__username__icontains=search) |
            Q(doctor__user__first_name__icontains=search) |
            Q(doctor__user__last_name__icontains=search)
        )

    # Filter by Status
    if status:
        recent_appointments = recent_appointments.filter(
            status=status
        )

    # Filter by Date
    if selected_date:
        recent_appointments = recent_appointments.filter(
            appointment_date=selected_date
        )

    # Latest 10 Appointments
    recent_appointments = recent_appointments.order_by(
        "-appointment_date",
        "-appointment_time"
    )[:10]

    # Revenue
    revenue = Appointment.objects.filter(
        status="COMPLETED"
    ).aggregate(
        total=Sum("doctor__consultation_fee")
    )["total"] or 0

    context = {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,

        "pending": pending,
        "confirmed": confirmed,
        "completed": completed,
        "cancelled": cancelled,

        "available_doctors": available_doctors,
        "unavailable_doctors": unavailable_doctors,

        "today_appointments": today_appointments,
        "recent_appointments": recent_appointments,

        "revenue": revenue,

        # Search Values
        "search": search,
        "selected_status": status,
        "selected_date": selected_date,
    }

    return render(
        request,
        "dashboard/admin_dashboard.html",
        context,
    )
    
@staff_member_required
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )
    appointment.status = "CONFIRMED"
    appointment.save()
    messages.success(
        request,
        "Appointment confirmed successfully."
    )
    return redirect("admin_dashboard")