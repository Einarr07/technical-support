from crum import get_current_user
from django.conf import settings
from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """
    Auditoria de tiempo
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """
    Auditoria de usuarios, quien creo y modifico
    """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_created',
        verbose_name='Creado por'
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='%(app_label)s_%(class)s_updated',
        verbose_name='Actualizado por'
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.created_by = user

        self.updated_by = user

        super().save(*args, **kwargs)


class AuditModel(TimeStampedModel, UserStampedModel):
    class Meta:
        abstract = True
