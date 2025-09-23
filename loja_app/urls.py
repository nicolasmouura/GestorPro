from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lojas, name='lista_lojas'),  # listar lojas
    path('cadastrar/', views.cadastrar_loja, name='cadastrar_loja'),  # cadastrar
    path('excluir/<int:pk>/', views.excluir_loja, name='excluir_loja'),  # excluir
]
