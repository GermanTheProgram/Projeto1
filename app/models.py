from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
