from django.db import models
from django.contrib.auth.models import User

from organizations.models import CareOrganization
from children.models import Child


class WishlistItem(models.Model):

    organization = models.ForeignKey(
        CareOrganization,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )

    item_name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    quantity_needed = models.PositiveIntegerField(
        default=1
    )

    quantity_fulfilled = models.PositiveIntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to='wishlist/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    @property
    def remaining_quantity(self):
        return max(
            self.quantity_needed -
            self.quantity_fulfilled,
            0
        )

    @property
    def is_fulfilled(self):
        return self.remaining_quantity == 0

    def __str__(self):
        return self.item_name


class Gift(models.Model):

    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('delivered', 'Delivered'),
        ('used', 'Used'),
    ]

    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='gifts'
    )

    wishlist_item = models.ForeignKey(
        WishlistItem,
        on_delete=models.CASCADE,
        related_name='gifts'
    )

    child = models.ForeignKey(
        Child,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='sent'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    anniversary_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.wishlist_item.item_name