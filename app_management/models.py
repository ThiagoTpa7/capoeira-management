from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)

    graduacao = models.CharField(max_length=50, blank=True, null=True)
    corda = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome


class Mensalidade(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Não pago'),
        ('PAGO', 'Pago'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    mes_referencia = models.CharField(max_length=7)  # ex: 04/2026
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    data_pagamento = models.DateField(null=True, blank=True)

    observacao = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['aluno', 'mes_referencia']

    def __str__(self):
        return f"{self.aluno.nome} - {self.mes_referencia}"
    
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    local = models.URLField(blank=True, null=True)

    imagem = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.data}"