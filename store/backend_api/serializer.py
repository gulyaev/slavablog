from rest_framework import serializers
from .models import SchoolSubject, SubjectCategory

class SubjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCategory
        fields = ['name', 'description']

class SchoolSubjectSerializer(serializers.ModelSerializer):
    category = SubjectCategorySerializer()
    
    class Meta:
        model = SchoolSubject
        fields = ['title', 'description', 'category']