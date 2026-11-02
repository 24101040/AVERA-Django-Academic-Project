from django.db import models
from django.contrib.auth.models import User

GIFT_CHOICES = [
    ('Books', 'Books'),
    ('Toys', 'Toys'),
    ('Clothes', 'Clothes'),
    ('Food Package', 'Food Package'),
    ('Educational Materials', 'Educational Materials'),
]

class SupporterFeedback(models.Model):
    supporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    supporter_name = models.CharField(max_length=100, blank=True, null=True)  # Name option
    gift = models.CharField(max_length=100, choices=GIFT_CHOICES, null=True, blank=True)
    comment = models.TextField()
    proof_image = models.ImageField(upload_to='proofs/', null=True, blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.supporter_name or 'Guest'}"