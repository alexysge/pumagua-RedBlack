from django.db import models

# Create your models here.
class bebederos(models.Model):
    var_estado = (
       ( '0', 'No disponible'),
       ( '1', 'Disponible'),
       ( '2', 'En mantenimiento'),
    )
    id_bebedero = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 100, blank = True)
    institucion = models.CharField(max_length = 100, blank = True)
    palabras_clave = models.CharField(max_length = 500, blank = True)
    descripcion = models.CharField(max_length = 1000, blank = True, default = '')
    latitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)
    longitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)
    estado = models.CharField(default='1', help_text="EstadoBebedero",max_length=1, choices=var_estado)

    def __str__(self):
        return f'Nombre: {self.nombre} Ubicacion: {self.ubicacion}'

class Reporte(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    bebedero = models.ForeignKey(bebederos, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    dato_extra = models.CharField(max_length = 200, blank = True, default = '')
    descripcion = models.CharField(max_length = 1000, blank = True, default = '')

    def __str__(self):
        return f'Reporte de {self.bebedero.nombre} hecho por ({self.nombre}) ({self.email})'

