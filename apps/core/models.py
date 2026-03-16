from django.core.exceptions import ValidationError
from django.db import models

from apps.common.models import AuditModel


# Create your models here.

def validate_email(value):
    if not value.endswith('@example.com'):
        raise ValidationError('Email address is not valid. The email must end with "@example.com".')

    return value


class Person(AuditModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, validators=[validate_email])
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(Person):
    department = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Technician(Person):
    gender = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Technican'
        verbose_name_plural = 'Technicans'
