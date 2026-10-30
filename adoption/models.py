from django.db import models

class AdoptionInformation(models.Model):
    CATEGORY_CHOICES = [
        ('process', 'Adoption Process'),
        ('eligibility', 'Eligibility'),
        ('documents', 'Required Documents'),
        ('support', 'Support & Guidance'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title