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
from .forms import DoctorForm

@method_decorator(staff_member_required, name="dispatch")
class DoctorListView(ListView):
    model = DoctorProfile
    template_name = "clinic_/doctor_list.html"
    context_object_name = "doctors"
    queryset = DoctorProfile.objects.select_related("user")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorCreateView(CreateView):
    model = DoctorProfile
    form_class = DoctorForm
    template_name = "clinic_/doctor_form.html"
    success_url = reverse_lazy("doctor_list")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorUpdateView(UpdateView):
    model = DoctorProfile
    form_class = DoctorForm
    template_name = "clinic_/doctor_form.html"
    success_url = reverse_lazy("doctor_list")
    
@method_decorator(staff_member_required, name="dispatch")
class DoctorDeleteView(DeleteView):
    model = DoctorProfile
    template_name = "clinic_/doctor_confirm_delete.html"
    success_url = reverse_lazy("doctor_list")