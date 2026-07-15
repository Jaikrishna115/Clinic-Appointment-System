# 🏥 Clinic Appointment System

A full-stack web application built with **Django** that allows patients to book appointments with doctors, enables doctors to manage their appointments, and provides administrators with a centralized dashboard to manage the system.

---

## 📌 Project Overview

The Clinic Appointment System simplifies the appointment booking process by providing dedicated dashboards for Patients, Doctors, and Administrators.

The application follows Django's MVC (MVT) architecture and implements authentication, role-based access, CRUD operations, search, filtering, pagination, and appointment management.

---

# ✨ Features

## 👤 Patient Module

- Patient Registration
- Secure Login & Logout
- Book Appointment
- View Appointment History
- Cancel Pending Appointments
- Patient Dashboard
- Change Password

---

## 👨‍⚕️ Doctor Module

- Doctor Dashboard
- View Assigned Appointments
- Confirm Appointments
- Complete Appointments
- Appointment Statistics
- Search Patients
- Filter by Status
- Filter by Appointment Date
- Pagination

---

## 👨‍💼 Admin Module

- Admin Dashboard
- Add Doctor
- Update Doctor Details
- Delete Doctor
- View All Doctors
- Dashboard Statistics
- Recent Appointments

---

# 🔐 Authentication

- User Registration
- Login
- Logout
- Password Change
- Protected Routes using `@login_required`
- Django Authentication System

---

# 📊 Dashboard Features

### Patient Dashboard

- Total Appointments
- Pending
- Confirmed
- Completed
- Appointment History

---

### Doctor Dashboard

- Total Patients
- Pending
- Confirmed
- Completed
- Search
- Filters
- Pagination

---

### Admin Dashboard

- Total Doctors
- Total Patients
- Total Appointments
- Recent Appointments

---

# 🛠️ Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Database

- postgre

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Clinic Appointment System/
│
├── accounts/
├── clinic_/
├── dashboard/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/jaikrishna115/Clinic-Appointment-System.git
```

Move into the project folder

```bash
cd Clinic-Appointment-System
```

Create Virtual Environment

```bash
python -m venv clinic
```

Activate Environment

### Windows

```bash
clinic\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 📸 Screenshots

Add screenshots here after deployment.

Example:

- Home Page
- Login Page
- Registration Page
- Patient Dashboard
- Doctor Dashboard
- Admin Dashboard
- Book Appointment
- Doctor Management

---

# 📚 Django Concepts Used

- Models
- ModelForms
- Views
- URL Routing
- Templates
- Template Inheritance
- Authentication
- Authorization
- Decorators
- Class Based Views
- Function Based Views
- CRUD Operations
- QuerySets
- `select_related()`                      
- Pagination
- Search
- Filtering
- Messages Framework

---

# 🔮 Future Enhancements

- Email Notifications
- SMS Notifications
- Online Payment Integration
- Medical Records
- Prescription Management
- Video Consultation
- Appointment Reminder
- Doctor Availability Calendar

---

# 👨‍💻 Author

**Jai Krishna**

- GitHub: https://github.com/jaikrishna115
- LinkedIn: *https://www.linkedin.com/in/jai-krishna-27b6013a0/*

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.