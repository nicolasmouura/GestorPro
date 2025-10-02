from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lojas, name='listar_lojas'),
    path('cadastrar/', views.cadastrar_loja, name='cadastrar_loja'),
    path('editar/<int:pk>/', views.editar_loja, name='editar_loja'),
    path('excluir/<int:pk>/', views.excluir_loja, name='excluir_loja'),
]


