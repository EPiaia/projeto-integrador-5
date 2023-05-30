from django.shortcuts import render, redirect
from pi5.models import *

def racas(request):
    if request.method == 'POST':
        tipo = Tipo.objects.get(id=request.POST['tipo'])
        descricao = request.POST['descricao'].strip()

        raca = Raca(
            tipo = Tipo.objects.get(id=request.POST['tipo']),
            descricao = request.POST['descricao'].strip()
        )
        raca.save()
        return redirect('racas')
    else:
        tipos = Tipo.objects.all()
        racas = Raca.objects.all()
    
        context = {
            "tipos": tipos,
            "racas": racas
        }

        return render(request, "racas.html", context)