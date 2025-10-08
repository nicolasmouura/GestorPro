from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lojas/', views.lista_lojas, name='lista_lojas'),
    path('lojas/cadastrar/', views.cadastrar_loja, name='cadastrar_loja'),
    path('lojas/editar/<int:id>/', views.editar_loja, name='editar_loja'),
    path('lojas/excluir/<int:id>/', views.excluir_loja, name='excluir_loja'),
]
