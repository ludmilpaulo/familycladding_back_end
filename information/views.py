from rest_framework import generics
from django.core.cache import cache
from django.db.models import Prefetch
from .models import Image, Carousel, AboutUs, Why_Choose_Us, Team, Contact
from .serializers import ImageSerializer, CarouselSerializer, AboutUsSerializer, WhyChooseUsSerializer, TeamSerializer, ContactSerializer

# ListCreateAPIView for creating and listing all instances
class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CarouselListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CarouselSerializer
    
    def get_queryset(self):
        cache_key = 'carousel_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Carousel.objects.prefetch_related('image').all()
            cache.set(cache_key, queryset, 300)  # Cache for 5 minutes
        return queryset

class AboutUsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AboutUsSerializer
    
    def get_queryset(self):
        cache_key = 'aboutus_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = AboutUs.objects.all()
            cache.set(cache_key, queryset, 600)  # Cache for 10 minutes
        return queryset

class WhyChooseUsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WhyChooseUsSerializer
    
    def get_queryset(self):
        cache_key = 'whychooseus_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Why_Choose_Us.objects.all()
            cache.set(cache_key, queryset, 600)  # Cache for 10 minutes
        return queryset

class TeamListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    
    def get_queryset(self):
        cache_key = 'team_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Team.objects.all()
            cache.set(cache_key, queryset, 600)  # Cache for 10 minutes
        return queryset

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# RetrieveUpdateDestroyAPIView for retrieving, updating and deleting a single instance
class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CarouselRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class AboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class WhyChooseUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Why_Choose_Us.objects.all()
    serializer_class = WhyChooseUsSerializer

class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
  
  # views.py

from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
 