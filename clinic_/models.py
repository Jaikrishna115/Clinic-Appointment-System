from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    
    def __str__(self):
        return self.user.username
    
class DoctorProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    SPECIALIZATION_CHOICES = [
    ("GENERAL", "General Physician"),
    ("DENTAL", "Dental"),
    ("EYE", "Eye Specialist"),
    ("ENT", "ENT"),
    ("ORTHO", "Orthopedic"),
]
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)
    qualifications = models.CharField(max_length=100, choices=[('MBBS', 'MBBS'), ('MD', 'MD'), ('DO', 'DO'), ('BDS', 'BDS'), ('MDS', 'MDS')])
    experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.username}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("COMPLETED", "Completed"),
    ("CANCELLED", "Cancelled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" {self.patient.user.username} with Dr. {self.doctor.user.username} on {self.appointment_date} at {self.appointment_time}"