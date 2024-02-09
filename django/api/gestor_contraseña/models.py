from django.db import models

# Aqui creo mi clase, que es donde se basa todo el proyecto

class Contraseña(models.Model):
    usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.usuario} - {self.contrasena}"
