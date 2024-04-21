# testimonials/views.py
from rest_framework import generics
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialListCreate(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
