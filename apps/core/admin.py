from django.contrib import admin

from apps.core.models import Customer, Technician

# Register your models here.
admin.site.register(Customer)
admin.site.register(Technician)
