from django.urls import path
#from . import views
#from .views import IndexPageView, indexV, agregarV, modificarV, listarV
from .views import registro_view, login_view, logout_view, \
    eliminarlaboratorio_view, agregar_laboratorio_view, \
    editar_laboratorio_view, \
    aa0V, aa1V

urlpatterns = [
    path('aa1/editar-laboratorio/<int:id>/', editar_laboratorio_view, name='editar_laboratorio'),
    path('agregar-laboratorio/', agregar_laboratorio_view, name='agregar_laboratorio'),
    path('aa1/eliminarlaboratorio/<id>', eliminarlaboratorio_view, name='eliminarlaboratorio'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', aa0V, name ='aa0'),
    path('aa1/', aa1V, name ='aa1'),
]

