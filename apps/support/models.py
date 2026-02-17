from django.db import models

from apps.common.models import AuditModel
from apps.core.models import Customer, Technician


# Create your models here.
class Ticket(AuditModel):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='tickets',
    )

    technical = models.ForeignKey(
        Technician,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
    )

    def __str__(self):
        return f'Ticket {self.code}'
