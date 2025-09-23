from django.db import models

# Create your models here.

from django.db import models

class Loja(models.Model):
    cnpj_loja = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cnpj_loja})"
