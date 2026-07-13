from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('profile/',views.profile, name="profile" ),
    path("change-password/",auth_views.PasswordChangeView.as_view(template_name="accounts/change_password.html"),name="change_password",),
    path("change-password/done/",auth_views.PasswordChangeDoneView.as_view(template_name="accounts/change_password_done.html"),name="password_change_done",),
    ]