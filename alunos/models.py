from django.db import models

# modelo Aluno

class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=50)
    email = models.EmailField("E-mail", unique=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['sobrenome', 'nome']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

# modelo Curso

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    alunos = models.ManyToManyField('Aluno', related_name='cursos') #um aluno pode estar matriculado em muitos cursos

    def __str__(self):
        return self.titulo