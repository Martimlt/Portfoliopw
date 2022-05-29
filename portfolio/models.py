from django.db import models


# Create your models here.

class Pessoa(models.Model):
    primeiroNome = models.CharField(max_length=100)
    ultimoNome = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=500)
    outroLink = models.URLField(max_length=500)
    professor = models.BooleanField(default=False)
    aluno = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.primeiroNome} {self.ultimoNome}"


class Competencia(models.Model):
    competencia = models.CharField(max_length=50)
    valor = models.IntegerField()
    softskill = models.BooleanField()

    def __str__(self):
        return f"{self.competencia}"


class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ranking = models.IntegerField()
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    professorAuxiliar = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')
    linklusofona = models.URLField()

    def __str__(self):
        return f"{self.nome}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    linkGit = models.URLField(max_length=500)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    ano = models.IntegerField()
    imagem = models.ImageField()
    tecnologia = models.CharField(max_length=100)
    participante = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name='+')
    left = models.BooleanField(default=False)
    right = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo}"


class Elogio(models.Model):
    primeiroNome = models.CharField(max_length=100)
    ultimoNome = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=200)
    elogio = models.CharField(max_length=800)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.primeiroNome} {self.ultimoNome}"


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    corpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    data = models.DateField(auto_created=False)
    urlnoticia = models.URLField()

    def __str__(self):
        return f"{self.titulo}"

