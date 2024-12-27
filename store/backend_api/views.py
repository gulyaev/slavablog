from django.shortcuts import render
from rest_framework.views import APIView
from .models import SchoolSubject, SubjectCategory
from .serializer import SchoolSubjectSerializer
from rest_framework.response import Response

def subjects(request):
    context = {
        'title': 'Разделы',
        'subjects': SchoolSubject.objects.all(),
        'categories': SubjectCategory.objects.all(),
    }
    return render(request, 'subjects/subjects.html', context)

# Create your views here.
class SchoolSubjectView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "description": output.description
            } for output in SchoolSubject.objects.all()
        ]
        return Response(output)

    def post (self, request):
        serializer = SchoolSubjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

