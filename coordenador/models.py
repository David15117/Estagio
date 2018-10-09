from django.db import models

#------------------------------
##########Base Coordenador#######
#------------------------------
#cadastrando Coordenador
class Coordenador(models.Model):
    class Meta:#Meta colocar nome nos admins
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'

    nome = models.CharField(max_length=60)
    cgu = models.IntegerField()
    def __str__(self):
        return self.nome

#cadastrando Orientador
class Orientador(models.Model):
    class Meta:#Meta colocar nome nos admins
        verbose_name = 'Orientador'
        verbose_name_plural = 'Orientadores'

    nome = models.CharField(max_length=60)
    cgu = models.IntegerField()

    def __str__(self):
        return self.nome

#cadastrando Orientando
class Orientando(models.Model):
    class Meta:
        verbose_name = 'Orientando'
        verbose_name_plural = 'Orientandos'
    nome = models.CharField(max_length=60)
    cgu = models.IntegerField()

    def __str__(self):
        return self.nome+' | '+str(self.cgu)

#Adicionar Acompanhamentos
class Acompanhamento(models.Model):
    class Meta:
        verbose_name = 'Acompanhamento'
        verbose_name_plural = 'Acompanhamentos'
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE,null=True, blank=True)
    orientando = models.OneToOneField(Orientando, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.orientador.nome

#adicionar data orientação coordenador
class Calendario(models.Model):
    class Meta:
        verbose_name = 'Calendario'
        verbose_name_plural = 'Calendarios'

    tipo = (
        ('E','Estagio supervisionado'),
        ('T', 'Trabalho de Conclução 1'),
        ('T2', 'Trabalho de Conclução 2'),
    )
    tipo = models.CharField(max_length=2, choices=tipo,null=True, blank=True)
    data = models.DateField()
    assunto = models.TextField(max_length=160,null=True, blank=True)

    def __str__(self):
        return self.tipo
