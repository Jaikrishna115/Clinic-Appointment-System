from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import DoctorProfile
from .forms import DoctorRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

@method_decorator(staff_member_required, name="dispatch")
class DoctorListView(ListView):
    model = DoctorProfile
    template_name = "clinic_/doctor_list.html"
    context_object_name = "doctors"
    queryset = DoctorProfile.objects.select_related("user")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorCreateView(CreateView):
    model = DoctorProfile
    form_class = DoctorRegistrationForm
    template_name = "clinic_/doctor_form.html"
    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        DoctorProfile.objects.create(
            user=user,
            specialization=form.cleaned_data["specialization"],
            qualifications=form.cleaned_data["qualifications"],
            experience=form.cleaned_data["experience"],
            consultation_fee=form.cleaned_data["consultation_fee"],
            is_available=form.cleaned_data["is_available"],
        )
        messages.success(
            self.request,
            "Doctor added successfully."
        )
        return redirect("doctor_list")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorUpdateView(UpdateView):
    model = DoctorProfile
    form_class = DoctorRegistrationForm
    template_name = "clinic_/doctor_form.html"
    success_url = reverse_lazy("doctor_list")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorDeleteView(DeleteView):
    model = DoctorProfile
    template_name = "clinic_/doctor_confirm_delete.html"
    success_url = reverse_lazy("doctor_list")