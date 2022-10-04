
from django.db import models


class Livro(models.Model):
    titulo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    imagem = models.ImageField(upload_to='media/%Y/%m/%d/')

    slug = models.SlugField(
        max_length = 255,
    )
    
    autor = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        max_length=10000,
        null=False,
        blank=False
    )

    genero = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    qntd_livro = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    data_lancamento = models.DateField(
        null=True,
        blank=True,
    )


'''
class Photo(models.Model):
    photo = models.ImageField('foto', uptload_to='')
    livro_capa = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        verbose_name = 'capa',
        related_name = 'photos',
        null = True,
        blank=True,
    )
    
    class Meta:
        ordering = ('pk',)
        verbose_name = 'capa'
        verbose_name_plural = 'capas'

    def __str__(self):
        return str(self.person)'''