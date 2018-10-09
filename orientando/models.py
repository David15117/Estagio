# Create your models here.
from django.db import models
from coordenador.models import Orientador
from coordenador.models import Orientando
from historico.models import LinhaDotempo

class Tempo(models.Model):
    class Meta:
        verbose_name = 'Historico Orientando'
        verbose_name_plural = 'Historicos Orientando'
    data = models.DateField(null=True, blank=True)
    linhadotempo = models.ForeignKey(LinhaDotempo, on_delete=models.CASCADE, null=True, blank=True)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo

