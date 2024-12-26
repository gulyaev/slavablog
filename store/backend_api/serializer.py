from rest_framework import serializers
from .models import SchoolSubject

class SchoolSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSubject
        fields = ['title', 'description',]