from django.db import models
from usuarios.models import CustomUser

class Propiedad(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name='propiedades', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    num_habitaciones = models.PositiveIntegerField()
    num_baños = models.PositiveIntegerField()
    imagen_principal = models.ImageField(upload_to='propiedades')
    imagenes_360 = models.ManyToManyField('Imagen360', blank=True)

    def __str__(self):
        return f"Propiedad en {self.direccion} - Precio: {self.precio}"

class Imagen360(models.Model):
    imagen = models.ImageField(upload_to='propiedades/360')
    imagen = models.ImageField(upload_to='propiedades/360')

    def __str__(self):
        return f"Imagen 360 de la propiedad"
