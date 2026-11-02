from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=20, default='ADOPTED IN 2026')
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title