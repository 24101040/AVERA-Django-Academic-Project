from django.db import models

class CareOrganization(models.Model):

    name = models.CharField(
        max_length=200
    )

    address = models.CharField(
        max_length=300
    )

    contact_number = models.CharField(
        max_length=30
    )

    email = models.EmailField()

    description = models.TextField()

    logo = models.ImageField(
        upload_to='organizations/',
        blank=True,
        null=True
    )

    verification_status = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name