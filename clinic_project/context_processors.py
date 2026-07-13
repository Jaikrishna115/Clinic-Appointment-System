def user_roles(request):
    return {
        "is_patient": hasattr(request.user, "patientprofile"),
        "is_doctor": hasattr(request.user, "doctorprofile"),
    }