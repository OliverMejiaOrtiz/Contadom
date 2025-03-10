from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('registros.urls', 'registros'), namespace='registros')),  # Incluir con namespace explícito
    # ...otras rutas existentes...
]