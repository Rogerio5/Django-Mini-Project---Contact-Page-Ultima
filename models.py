from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"


class Reserva(models.Model):
    pet_nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet_nome} - {self.data}"


# Create your models here.
