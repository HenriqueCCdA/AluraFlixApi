from django.db import models
from django.urls import resolve


class CreationModificationBase(models.Model):

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


class Categoria(CreationModificationBase):
    titulo = models.CharField(max_length=60)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return f'/categorias/{self.pk}'
        return resolve('core:')


class Video(CreationModificationBase):

    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    url = models.URLField()
    categoria = models.ForeignKey('Categoria', related_name='videos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo
