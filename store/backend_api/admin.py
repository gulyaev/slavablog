from django.contrib import admin

# Register your models here.
from backend_api.models import SchoolSubject, SubjectCategory

admin.site.register(SchoolSubject)
admin.site.register(SubjectCategory)

