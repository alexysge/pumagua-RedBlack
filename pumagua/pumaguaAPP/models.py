from django.db import models

# Create your models here.
class bebederos(models.Model):
    id_bebedero = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 100, blank = True)
    institucion = models.CharField(max_length = 100, blank = True)
    palabras_clave = models.CharField(max_length = 500, blank = True)
    descripcion = models.CharField(max_length = 1000, blank = True, default = '')
    latitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)
    longitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)

    def __str__(self):
        return f'Nombre: {self.nombre} Ubicacion: {self.ubicacion}'
