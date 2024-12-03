from django.contrib.auth.models import User
from django.db import models

# Modelo para o jogo
class Jogo(models.Model):
    STATUS_CHOICES = [
        ('quero_jogar', 'Quero Jogar'),
        ('abandonado', 'Abandonado'),
        ('jogando', 'Jogando'),
        ('zerado', 'Zerado'),
    ]
    
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='quero_jogar')  # Campo de status
    
    def __str__(self):
        return self.titulo

# Modelo para avaliação do jogo
class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)  # Corrigido para 'ForeignKey' sem 'models.models'
    nota = models.IntegerField()
    comentario = models.TextField()
    
    def __str__(self):
        return f'{self.usuario.username} - {self.jogo.titulo}'

# Modelo para tempo de jogo
class TempoDeJogo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    tempo = models.FloatField()  # tempo em horas
    
    def __str__(self):
        return f'{self.usuario.username} - {self.jogo.titulo} - {self.tempo}h'

# Modelo para tags de jogos
class Tag(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)  # tag do jogo
    
    def __str__(self):
        return f'{self.jogo.titulo} - {self.tag}'
