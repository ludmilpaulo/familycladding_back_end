from django.db import models

class ProjectImage(models.Model):
    image = models.ImageField(max_length=3000, default='', blank=True, upload_to='carousel_images/')

    def __str__(self):
        return self.image.name if self.image else ''

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    pictures = models.ManyToManyField(ProjectImage)

    def __str__(self):
        return self.name
