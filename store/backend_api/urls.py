from django.urls import path
from backend_api.views import subjects
app_name = 'backend_api'

urlpatterns = [
    path('', subjects, name = 'index'),
]