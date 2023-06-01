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
    
def editarRaca(request, id):
    raca = Raca.objects.get(id=id)
    if request.method == 'POST':
        raca.tipo = Tipo.objects.get(id=request.POST['tipo'])
        raca.descricao = request.POST['descricao'].strip()
        raca.save()
        return redirect('racas')
    else:
        tipos = Tipo.objects.all()
        racas = Raca.objects.all()
    
        context = {
            "tipos": tipos,
            "racas": racas,
            "raca": raca
        }

        return render(request, "racas.html", context)
    
def excluirRaca(request, id):
    raca = Raca.objects.get(id=id)
    raca.delete()
    return redirect('racas')
    
def index(request):
    return render(request, "index.html")

def adocao(request):
    return render(request, "adocao.html")

def adotar(request):
    return render(request, "adotar.html")

def animais(request):
    if request.method == 'POST':
        animal = Animal(
            nome = request.POST['nome'].strip(),
            observacao = request.POST['observacoes'].strip(),
            situacao = Situacao.objects.get(id=request.POST['situacao']),
            raca = Raca.objects.get(id=request.POST['raca'])
        )
        animal.save()
        return redirect('animais')
    else:
        animais = Animal.objects.all()
        racas = Raca.objects.all()
        situacoes = Situacao.objects.all()

        context = {
            "animais": animais,
            "racas": racas,
            "situacoes": situacoes
        }

        return render(request, "animais.html", context)
    
def excluirAnimal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return redirect('animais')

def editarAnimal(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == 'POST':
        animal.nome = request.POST['nome'].strip()
        animal.raca = Raca.objects.get(id=request.POST['raca'])
        animal.situacao = Situacao.objects.get(id=request.POST['situacao'])
        animal.observacao = request.POST['observacoes'].strip()
        animal.save()
        return redirect('animais')
    else:
        situacoes = Situacao.objects.all()
        racas = Raca.objects.all()
        animais = Animal.objects.all()
    
        context = {
            "animal": animal,
            "animais": animais,
            "racas": racas,
            "situacoes": situacoes
        }

        return render(request, "animais.html", context)

def cadastro(request):
    return render(request, "cadastro.html")

def denuncias(request):
    return render(request, "denuncias.html")

def login(request):
    return render(request, "login.html")

def pessoas(request):
    return render(request, "pessoas.html")

def relatorioDenuncias(request):
    return render(request, "relatorioDenuncias.html")

def relatorioResgates(request):
    return render(request, "relatorioResgates.html")

def resgates(request):
    return render(request, "resgates.html")