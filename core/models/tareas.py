from django.db import models

class Tareas(models.Model):

    titulo=models.CharField('titulo', max_length=35)
    descripcion = models.CharField('descripcion', max_length=255)
    activo = models.IntegerField('activo')
    fecha_ejecucion = models.DateField('fecha ejecucion',  
        help_text="Date execution")
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text="Date time on"
        )
    def __str__(self):
	    return self.id