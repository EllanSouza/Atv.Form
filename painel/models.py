from django.db import models

LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Estudante(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    data_nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO, default='Feminino')
    minicursos = models.ManyToManyField(MiniCurso)

    def __str__(self):
        return self.nome