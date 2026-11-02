from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_TYPES = [
        ('supporter', 'Supporter'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='supporter'
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username


from django.db import models

# Create your models here.
