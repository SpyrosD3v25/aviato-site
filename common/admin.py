from django.contrib import admin
from .models import User, NormalUser, Dietician, Doctor, PersonalTrainer

class NormalUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'sex', 'weight']

class DieticianAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'expertise']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'specialization']

class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'certification']

admin.site.register(User)
admin.site.register(NormalUser, NormalUserAdmin)
admin.site.register(Dietician, DieticianAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(PersonalTrainer, PersonalTrainerAdmin)
