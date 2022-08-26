from django.urls import path
from Database.views import inicio,Nosotros,contacto

urlpatterns = [
   path('', inicio),
   path('Nosotros',Nosotros),

   path('contacto',contacto),


]