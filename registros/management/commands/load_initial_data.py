from django.core.management.base import BaseCommand
from django.db import connection
from registros.models import Cuenta, Categoria_ecuacion_contable, Transaccion, DetalleTransaccion

class Command(BaseCommand):
    help = 'Limpia la base de datos y carga las cuentas iniciales'

    def handle(self, *args, **options):
        if input('¿Estás seguro de que deseas borrar todos los datos? (s/N): ').lower() != 's':
            self.stdout.write('Operación cancelada')
            return
        
        try:
            # Limpiar la base de datos
            self.stdout.write('Limpiando base de datos...')
            DetalleTransaccion.objects.all().delete()
            Transaccion.objects.all().delete()
            Cuenta.objects.all().delete()
            Categoria_ecuacion_contable.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Base de datos limpiada exitosamente'))

            # Cargar los datos
            self.stdout.write('Cargando datos...')
            with connection.cursor() as cursor:
                sql_file = 'registros/sql/insert_cuentas.sql'
                with open(sql_file, 'r', encoding='utf-8') as f:
                    sql_commands = f.read().split(';')
                    
                    for command in sql_commands:
                        command = command.strip()
                        if command:
                            try:
                                cursor.execute(command)
                                connection.commit()
                            except Exception as e:
                                self.stdout.write(
                                    self.style.ERROR(f'Error en comando SQL: {str(e)}')
                                )
                                self.stdout.write(f'Comando problemático: {command}')
                                raise

            # Verificar que se insertaron los datos
            num_categorias = Categoria_ecuacion_contable.objects.count()
            num_cuentas = Cuenta.objects.count()
            
            self.stdout.write(self.style.SUCCESS(
                f'Datos cargados exitosamente:\n'
                f'- Categorías insertadas: {num_categorias}\n'
                f'- Cuentas insertadas: {num_cuentas}'
            ))

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error durante la carga de datos: {str(e)}')
            )
