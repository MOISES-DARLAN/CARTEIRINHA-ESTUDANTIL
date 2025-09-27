from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('alunos.urls')),
    path('parceiros/', include('parceiros.urls')),
    path('suporte/', include('suporte.urls')),
    path('', include('core.urls')),
]