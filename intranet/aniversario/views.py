from django.shortcuts import render
from .models import Aniversariante

def ListaAniversariante(request):
    aniversariantes = Aniversariante.objects.all()
    return render(request,
                  'aniversario/lista.html', {'aniversariantes': aniversariantes})