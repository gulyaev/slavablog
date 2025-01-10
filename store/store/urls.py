from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from  django.conf import settings

from backend_api.views import *
# from store.backend_api.views import SchoolSubjectView
from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', SchoolSubjectView.as_view(), name='oh shit'),
    path('mainpageurokikz/', index, name = 'index'), #cmd+D
    # path('products/', products, name = 'products'),
    path('products/', include('products.urls', namespace = 'products')),
    path('subjects/', include('backend_api.urls', namespace = 'subjects')),
    path('users/', include('users.urls', namespace = 'users')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)