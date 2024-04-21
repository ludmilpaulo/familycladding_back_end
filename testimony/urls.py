# testimonials/urls.py
from django.urls import path
from .views import TestimonialListCreate, TestimonialRetrieveUpdateDestroy

urlpatterns = [
    path('testimonials/', TestimonialListCreate.as_view(), name='testimonial-list'),
    path('testimonials/<int:pk>/', TestimonialRetrieveUpdateDestroy.as_view(), name='testimonial-detail'),
]
