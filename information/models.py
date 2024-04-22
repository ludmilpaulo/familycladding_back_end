from django.db import models
from django.utils import timezone
from django.urls import reverse
import re
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

class Image(models.Model):
    image = models.ImageField(max_length=3000, default='', blank=True, upload_to='carousel_images/')

    def __str__(self):
        return self.image.name if self.image else ''


class Carousel(models.Model):
	image = models.ManyToManyField(Image)
	title = models.CharField(max_length=150)
	sub_title = models.CharField(max_length=100)

	def __str__(self):
		return self.title


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length = 50)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    backgroundImage = models.ImageField(upload_to="bg_logo/", blank=True, null=True)
    about = CKEditor5Field('Text', config_name='extends')
    born_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    # Social Network
    whatsapp = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)


    class Meta:
        verbose_name = 'about us '
        verbose_name_plural = 'about us '

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'why choose us '
        verbose_name_plural = 'why choose us '

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to='chef/')
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Squad'
        verbose_name_plural = 'Squad'

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    content = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.author





from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

class Contact(models.Model):
    subject = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    company = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    message = models.TextField(verbose_name='Conteúdo')
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, **kwargs):
    subject = "Thank you for contacting us!"
    message = f"""
    Thank you for contacting us!

    We have received your message and will get back to you as soon as possible.

    Here are the details you provided:
    - Name: {instance.name}
    - Email: {instance.email}
    - Company: {instance.company}
    - Address: {instance.address}
    - Phone: {instance.phone}

    We appreciate your interest and look forward to assisting you.

    Best regards,
    Family Cladding
    """
    sender_email = settings.EMAIL_HOST_USER  # Use the email host user as the sender
    recipient_email = instance.email
    send_mail(subject, message, sender_email, [recipient_email])
