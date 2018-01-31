from django.db import models


class Departamento(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=75)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=75)
    departamento = models.ForeignKey(Departamento, related_name='provincias',
                                     null=True, blank=True)

    def __str__(self):
        return self.nombre


class Distrito(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=75)
    provincia = models.ForeignKey(Provincia, related_name='distritos',
                                  null=True, blank=True)
    ubigeo = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Establecimiento(models.Model):
    nombre = models.CharField(verbose_name='Establecimiento', max_length=300, null=True, blank=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=500, null=True, blank=True)
    referencia = models.CharField(verbose_name='Referencia', help_text='Avenida,Calle,Cuadra de referecia',
                                  max_length=500, null=True, blank=True)
    tlf_1 = models.CharField(verbose_name='Teléfono Fijo', max_length=7, null=True, blank=True)
    tlf_2 = models.CharField(verbose_name='Teléfono Celular 1', max_length=9, null=True, blank=True)
    tlf_3 = models.CharField(verbose_name='Teléfono Celular 2', max_length=9, null=True, blank=True)
    correo = models.CharField(verbose_name='Correo', max_length=200, null=True, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7,
                                  verbose_name='Latitud', null=True,
                                  blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7,
                                   verbose_name='Longitud', null=True,
                                   blank=True)
    distrito = models.ForeignKey(Distrito, related_name='distritos', null=True, blank=True)
    # is_enabled = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/establecimiento', null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return '{}'.format(self.nombre)