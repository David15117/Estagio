from django.db import models

# Create your models here.
class Comentario(models.Model):
    arquivo = models.FileField(upload_to='documents/', null=True, blank=True)
    comentario = models.TextField(max_length=160,null=True, blank=True)

    def __str__(self):
        return  self.comentario