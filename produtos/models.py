from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    observacao = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nome+' | Quantidade: '+str(self.quantidade)