from django.urls import path
from . import views

app_name = 'registros'

urlpatterns = [
    path('', views.home, name='home'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('cuentas/', views.listar_cuentas, name='listar_cuentas'),
    path('cuentas/crear/', views.crear_cuenta, name='crear_cuenta'),
    path('cuentas/editar/<int:id_cuenta>/', views.editar_cuenta, name='editar_cuenta'),
    path('cuentas/eliminar/<int:id_cuenta>/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('transacciones/', views.listar_transacciones, name='listar_transacciones'),
    path('transacciones/ingresar/', views.ingresar_transaccion, name='ingresar_transaccion'),
    path('diario/', views.ver_diario, name='ver_diario'),
    path('mayor/', views.ver_mayor, name='ver_mayor'),
    path('balanzaComprobacion/', views.balanza_comprobacion, name='balanza_comprobacion'),
    path('estadoResultados/', views.estado_resultados, name='estado_resultados'),
    path('estadoCapitalContablePropietario/', views.estado_capital_contable_propietario, name='estado_capital_contable_propietario'),
    path('balanceGeneral/', views.estado_balance_general, name='estado_balance_general'),
    path('estadoFlujoEfectivo/', views.estado_flujo_efectivo, name='estado_flujo_efectivo'),
]
