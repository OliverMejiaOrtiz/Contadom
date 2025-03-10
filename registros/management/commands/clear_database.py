from django.core.management.base import BaseCommand
from registros.models import Cuenta, Categoria_ecuacion_contable, Transaccion, DetalleTransaccion

class Command(BaseCommand):
    help = 'Limpia todas las tablas de la base de datos'

    def handle(self, *args, **options):
        self.stdout.write('Limpiando base de datos...')
        
        DetalleTransaccion.objects.all().delete()
        Transaccion.objects.all().delete()
        Cuenta.objects.all().delete()
        Categoria_ecuacion_contable.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS('Base de datos limpiada exitosamente')
        )
