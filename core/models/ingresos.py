from django.db import models

class Ingreso(models.Model):

    name = models.CharField('nombre', max_length=50)
    descripcion = models.CharField('descripcion', max_length=255)
    valor = models.DecimalField('Dinero ingresado',max_digits=25,decimal_places=2)
    activo = models.IntegerField('activo')
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text="Date time on"
        )
    def __str__(self):
	    return self.id