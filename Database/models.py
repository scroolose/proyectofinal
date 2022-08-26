from django.db import models





class inicio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Nosotros(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class Contacto(models.Model):
    nombre = models.Model
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()



