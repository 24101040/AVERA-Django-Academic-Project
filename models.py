from django.db import models

from organizations.models import CareOrganization


class Child(models.Model):
    organization = models.ForeignKey(
        CareOrganization,
        on_delete=models.CASCADE,
        related_name='children'
    )

    display_name = models.CharField(
        max_length=100
    )

    age = models.PositiveIntegerField()

    general_description = models.TextField()

    photo = models.ImageField(
        upload_to='children/',
        blank=True,
        null=True
    )

    is_public = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.display_name


class Milestone(models.Model):
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='milestones'
    )

    title = models.CharField(
        max_length=200
    )

    update_text = models.TextField()

    update_date = models.DateField()

    photo = models.ImageField(
        upload_to='milestones/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
