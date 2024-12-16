# mysite/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, mundo!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ruta para la raíz del sitio
]
