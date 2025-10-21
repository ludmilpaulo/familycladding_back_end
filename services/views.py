from rest_framework import generics
from django.core.cache import cache
from .models import Service
from .serializers import ServiceSerializer

class ServiceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        cache_key = 'service_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Service.objects.all()
            cache.set(cache_key, queryset, 600)  # Cache for 10 minutes
        return queryset

class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
