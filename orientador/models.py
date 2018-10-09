from django.db import models
from coordenador.models import Orientador
from coordenador.models import Orientando
from historico.models import LinhaDotempo

# from tempo.models import LinhaDotempo
# Create your models here.
# ------------------------------
##########Base Orientador#######
# ------------------------------


class Reuniao(models.Model):
    class Meta:
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reuniões'

    data = models.DateField()
    assunto = models.TextField(max_length=130)
    orientando = models.ForeignKey(Orientando, on_delete=models.CASCADE, null=True, blank=True)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Assunto' + self.assunto


class Historico(models.Model):
    class Meta:
        verbose_name = 'Historico Orientador'
        verbose_name_plural = 'Historico Orientadores'
    linhadotempo=models.ForeignKey(LinhaDotempo, on_delete=models.CASCADE, null=True, blank=True)
    orientando = models.ForeignKey(Orientando, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.orientando.nome