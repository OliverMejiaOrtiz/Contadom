from django.db import models

CATEGORIAS = [
    ('ACTIVO', 'Activo'),
    ('PASIVO', 'Pasivo'),
    ('PATRIMONIO', 'Patrimonio'),
    ('INGRESOS', 'Ingresos'),
    ('COSTOS_GASTOS', 'Costos/Gastos'),
]

class Categoria_ecuacion_contable(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Cuenta(models.Model):
    id_cuenta = models.IntegerField(primary_key=True)  # Cambiado de AutoField a IntegerField
    nombre_cuenta = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(Categoria_ecuacion_contable, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_cuenta

class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    fecha_transaccion = models.DateField()
    glosa = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Asiento {self.id_transaccion} - {self.fecha_transaccion}"

    def total_debe(self):
        return sum(detalle.monto for detalle in self.detalles.filter(es_debe=True))

    def total_haber(self):
        return sum(detalle.monto for detalle in self.detalles.filter(es_debe=False))

class DetalleTransaccion(models.Model):
    transaccion = models.ForeignKey(Transaccion, related_name='detalles', on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    es_debe = models.BooleanField()

    def __str__(self):
        tipo = "DEBE" if self.es_debe else "HABER"
        return f"{self.cuenta.nombre_cuenta} - {tipo}: {self.monto}"
