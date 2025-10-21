# api/views.py
from rest_framework import generics
from django.core.cache import cache
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        cache_key = 'project_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Project.objects.prefetch_related('pictures').all()
            cache.set(cache_key, queryset, 300)  # Cache for 5 minutes
        return queryset

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
