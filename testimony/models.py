# testimonials/models.py
from django.db import models

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
