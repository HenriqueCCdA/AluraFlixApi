from django.db import models


class CreationModificationBase(models.Model):

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


class Video(CreationModificationBase):

    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.titulo
