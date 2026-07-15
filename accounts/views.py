from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm
from clinic_.models import PatientProfile
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()
            PatientProfile.objects.create(user=user,phone=form.cleaned_data['phone'],
                                          age=form.cleaned_data['age'],
                                          gender=form.cleaned_data['gender'],
                                          blood_group=form.cleaned_data['blood_group'],
                                          address=form.cleaned_data['address'],
                                          date_of_birth=form.cleaned_data['date_of_birth'])
            messages.success(
                request,"Registration completed successfully. Please login."
                             )
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):

    if request.method == "POST":

        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:

                login(request, user)

                if user.is_staff:
                    return redirect("admin_dashboard")

                elif hasattr(user, "doctorprofile"):
                    return redirect("doctor_dashboard")

                elif hasattr(user, "patientprofile"):
                    return redirect("patient_dashboard")

                else:
                    return redirect("home")

        messages.error(request, "Invalid username or password.")

    else:
        form = UserLoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")

@login_required
def profile(request):
    patient = request.user.patientprofile
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST,
            instance=patient
        )
        if form.is_valid():
            request.user.first_name = form.cleaned_data["first_name"]
            request.user.last_name = form.cleaned_data["last_name"]
            request.user.email = form.cleaned_data["email"]
            request.user.save()
            form.save()
            messages.success(request,"Profile Updated Successfully.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(
            instance=patient,
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            },
        )
    return render(request,"accounts/profile.html",{"form": form})

