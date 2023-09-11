'''

COMMON MODELS BETWEEN THE APPS.

'''

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    NORMAL_USER = 'NU'
    DIETICIAN = 'DT'
    DOCTOR = 'DR'	

    PERSONAL_TRAINER = 'PT'
    
    ROLE_CHOICES = [
        (NORMAL_USER, 'Normal User'),
        (DIETICIAN, 'Dietician'),
        (DOCTOR, 'Doctor'),
        (PERSONAL_TRAINER, 'Personal Trainer'),
    ]

    agree = models.BooleanField(default=False)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=NORMAL_USER)

    def __str__(self):
        return self.username

class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='normal_user')
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # Add other common user-related fields here (e.g., health problems, allergies)

    def __str__(self):
        return self.user.username

class Dietician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dietician')
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=100)
    # Add other fields for dieticians' information

    def __str__(self):
        return f"Dietician: {self.user.username}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    # Add other fields for doctors' information

    def __str__(self):
        return f"Doctor: {self.user.username}"

class PersonalTrainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_trainer')
    email = models.EmailField(unique=True)
    certification = models.CharField(max_length=100)
    # Add other fields for personal trainers' information

    def __str__(self):
        return f"Personal Trainer: {self.user.username}"
