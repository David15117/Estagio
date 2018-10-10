from django.shortcuts import render
from .models import Orientador
# Create your views here.
#Lista todos os orientadores do banco de dados
#Lista Orientandos e seus devidos orientadores, que tem como relacionamento a tabela acompanhamento
def orientador_list(request):
    orientador = Orientador.objects.all()
    print(orientador)
    return render(request, 'orientador_list.html', {'orientador':orientador,'acompanhamento':acompanhamento})


