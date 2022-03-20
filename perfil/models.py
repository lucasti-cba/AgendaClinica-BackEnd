import email
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=False, null=False)


class Peril(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    dataNascimento = models.DateField()
    foto = models.ForeignKey(Imagem, on_delete=models.CASCADE)


