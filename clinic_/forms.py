from django import forms
from django.contrib.auth.models import User
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
        

class DoctorRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )
    class Meta:
        model = DoctorProfile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "specialization",
            "qualifications",
            "experience",
            "consultation_fee",
            "is_available",
        ]
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already exists."
            )
        return username
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists."
            )
        return email
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password != confirm:
            raise forms.ValidationError(
                "Passwords do not match."
            )
        return cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.input_type == "checkbox":
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
    
class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            "specialization",
            "qualifications",
            "experience",
            "consultation_fee",
            "is_available",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.input_type == "checkbox":
               field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"