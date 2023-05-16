from django.db import models
class Person(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    acoes = models.CharField(max_length=30)
    def __str__(self):
        return self.nome + ' - ' + self.sobrenome
# Create your models here.
