from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from clinic_.models import PatientProfile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Last Name"}))
    email = forms.EmailField()
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Phone Number"}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], widget=forms.Select(attrs={"class":"form-select"}))
    blood_group = forms.ChoiceField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], widget=forms.Select(attrs={"class":"form-select"}))
    address = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows": 3, "placeholder": "Address"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',"class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'age', 'gender', 'blood_group', 'address', 'date_of_birth', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs = {"class": "form-control","placeholder": "username"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control","placeholder":"Password"}))
    
class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    class Meta:
        model = PatientProfile
        fields = [
            "phone",
            "age",
            "gender",
            "blood_group",
            "address",
            "date_of_birth",
        ]