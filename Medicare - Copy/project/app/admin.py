from django.contrib import admin
from .models import Contact, Appointment

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Contact)