from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    tipo = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
    def __str__(self):
        return self.tipo
    
class Situacao(models.Model):
    situacao = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"
    def __str__(self):
        return self.situacao
    
class Raca(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"
    def __str__(self):
        return self.descricao
    
class SolicitacaoResgate(models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length = 80)
    numero = models.CharField(max_length = 20)
    endereco = models.CharField(max_length = 100)
    observacao = models.CharField(max_length = 300)
    foto = models.ImageField(upload_to='solicitacoes_resgate')
    class Meta:
        verbose_name = "SolicitaçãoResgate"
        verbose_name_plural = "SolicitaçõesResgate"

class Denuncia(models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length = 80)
    numero = models.CharField(max_length = 20)
    endereco = models.CharField(max_length = 100)
    observacao = models.CharField(max_length = 300)
    foto = models.ImageField(upload_to='denuncias')
    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"
    
class Animal(models.Model):
    nome = models.CharField(max_length = 60)
    foto = models.ImageField(upload_to='animais')
    observacao = models.CharField(max_length = 200)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length = 120)
    email = models.CharField(max_length = 80)
    telefone = models.CharField(max_length = 20)
    cpf = models.CharField(max_length = 11)
    endereco = models.CharField(max_length = 300)
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
    def __str__(self):
        return self.nome

class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    observacao = models.CharField(max_length = 200)
    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"
    def __str__(self):
        return self.animal

