from django.db import models


# Create your models here.
class Produtos(models.Model):
    imagem = models.CharField(max_length=300, null=False, blank=False)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descrcao = models.CharField(max_length=300, null=False, blank=False)


def __str__(self):
    return f"Titulo [titulo={self.titulo}]"