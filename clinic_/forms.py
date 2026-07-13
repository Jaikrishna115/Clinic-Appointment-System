from django import forms
from .models import Appointment, DoctorProfile

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "appointment_date", "appointment_time", "reason"]
        widgets = {
            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control"
                }
            ),
            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Reason for Appointment"
                }
            ),
            "doctor": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = DoctorProfile.objects.filter(is_available=True)
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            "user",
            "specialization",
            "consultation_fee",
            "is_available",
        ]
        widgets = {
            "user": forms.Select(attrs={"class":"form-select"}),
            "specialization": forms.TextInput(attrs={"class":"form-control"}),
            "consultation_fee": forms.NumberInput(attrs={"class":"form-control"}),
            "is_available": forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }