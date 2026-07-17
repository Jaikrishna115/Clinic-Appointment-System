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
from .forms import DoctorRegistrationForm, DoctorForm, DoctorUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q

@method_decorator(staff_member_required, name="dispatch")
class DoctorListView(ListView):
    model = DoctorProfile
    template_name = "clinic_/doctor_list.html"
    context_object_name = "doctors"
    paginate_by = 10

    def get_queryset(self):
        queryset = DoctorProfile.objects.select_related("user")
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) |
                Q(specialization__icontains=search)
            )

        return queryset.order_by("user__first_name")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        context["total_doctors"] = DoctorProfile.objects.count()
        return context
        
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
    form_class = DoctorUpdateForm
    template_name = "clinic_/doctor_form.html"
    success_url = reverse_lazy("doctor_list")

    def form_valid(self, form):
        doctor = form.save(commit=False)
        doctor.save()
        messages.success(
        self.request,
        "Doctor updated successfully."
        )
        return redirect("doctor_list")
        
@method_decorator(staff_member_required, name="dispatch")
class DoctorDeleteView(DeleteView):
    model = DoctorProfile
    template_name = "clinic_/doctor_confirm_delete.html"
    success_url = reverse_lazy("doctor_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Doctor deleted successfully.")
        return super().delete(request, *args, **kwargs)