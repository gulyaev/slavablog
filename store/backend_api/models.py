from django.db import models

# Create your models here.
class SubjectCategory(models.Model):
    name = models.CharField(max_length=128, unique=True )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SchoolSubject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'Предмет: {self.title}'