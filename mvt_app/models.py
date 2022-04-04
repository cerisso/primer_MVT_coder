from django.db import models

# Create your models here.
class Familiares(models.Model):

    id = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
