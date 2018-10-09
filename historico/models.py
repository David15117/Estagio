from django.db import models
from coordenador.models import Orientador
from comentario.models import Comentario
from coordenador.models import Orientando
# Create your models here.
class LinhaDotempo(models.Model):
    class Meta:
        verbose_name = 'Linha Do tempo'
        verbose_name_plural = 'Linhas Do tempo'

    orientador= models.ForeignKey(Orientador, on_delete=models.CASCADE, null=True, blank=True)
    orientando = models.ForeignKey(Orientando, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.orientando.nome