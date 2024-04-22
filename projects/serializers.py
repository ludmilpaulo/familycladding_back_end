# api/serializers.py
from rest_framework import serializers
from .models import Project, ProjectImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['image']

class ProjectSerializer(serializers.ModelSerializer):
    pictures = ImageSerializer(many=True)
    class Meta:
        model = Project
        fields =[
        "id",
        "name",
        "description",
        "start_date",
        "end_date",
        "pictures"]
