from django.shortcuts import render, redirect
from pi5.models import *
from pi5.utils import *

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
    if request.method == 'POST':
        animal = Animal.objects.get(id=request.POST['animal'])
        pessoa = Pessoa.objects.get(id=request.POST['pessoa'])
        obs = request.POST['observacoes']

        adocao = Adocao(
            animal = animal,
            pessoa = pessoa,
            observacao = obs
        )
        adocao.save()
        
        sitAdotado = Situacao.objects.get(id=2)
        animal.situacao = sitAdotado
        animal.save()

        return redirect('adocao')
    else:
        adocoes = Adocao.objects.all()
        pessoas = Pessoa.objects.all()
        sitNaoAdotado = Situacao.objects.get(id=1)
        animais = Animal.objects.filter(situacao=sitNaoAdotado)

        context = {
            "adocoes": adocoes,
            "pessoas": pessoas,
            "animais": animais
        }

        return render(request, "adocao.html", context)
    
def excluirAdocao(request, id):
    adocao = Adocao.objects.get(id=id)

    sitNaoAdotado = Situacao.objects.get(id=1)
    animal = adocao.animal
    animal.situacao = sitNaoAdotado
    animal.save()

    adocao.delete()
    return redirect('adocao')

def editarAdocao(request, id):
    adocao = Adocao.objects.get(id=id)
    if request.method == 'POST':
        animalAntigo = adocao.animal
        animalNovo = Animal.objects.get(id=request.POST['animal'])
        if animalNovo != animalAntigo:
            sitNaoAdotado = Situacao.objects.get(id=1)
            sitAdotado = Situacao.objects.get(id=2)
            animalAntigo.situacao = sitNaoAdotado
            animalNovo.situacao = sitAdotado
            animalAntigo.save()
            animalNovo.save()
        adocao.animal = animalNovo
        adocao.pessoa = Pessoa.objects.get(id=request.POST['pessoa'])
        adocao.observacao = request.POST['observacoes']
        adocao.save()
        return redirect('adocao')
    else:
        adocoes = Adocao.objects.all()
        sitNaoAdotado = Situacao.objects.get(id=1)
        animais = Animal.objects.filter(situacao=sitNaoAdotado)
        pessoas = Pessoa.objects.all()
    
        context = {
            "adocao": adocao,
            "adocoes": adocoes,
            "animais": animais,
            "pessoas": pessoas
        }

        return render(request, "adocao.html", context)

def adotar(request):
    situacaoNaoAdotado = Situacao.objects.get(id=1)
    animais = Animal.objects.filter(situacao=situacaoNaoAdotado)

    linhas = []
    linha = Linha()
    count = 0
    countLinhas = 0
    for animal in animais:
        if count == 3:
            count = 0
            linhas.append(linha)
            linha = Linha()
            countLinhas += 1
        linha.animais.append(animal)
        count += 1

        v = int(animais.count()/3)
        resto = animais.count() - (v * 3)

        if count == resto and countLinhas == v:
            linhas.append(linha)

    context = {
        "linhas": linhas
    }

    return render(request, "adotar.html", context)

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
    if request.method == 'POST':
        denuncia = Denuncia (
            nome = request.POST['nome'].strip(),
            email = request.POST['email'].strip(),
            numero = request.POST['telefone'].strip(),
            endereco = request.POST['endereco'].strip(),
            observacao = request.POST['observacoes'].strip()
        )
        denuncia.save()
    return render(request, "denuncias.html")

def resgates(request):
    if request.method == 'POST':
        solicResgate = SolicitacaoResgate (
            nome = request.POST['nome'].strip(),
            email = request.POST['email'].strip(),
            numero = request.POST['telefone'].strip(),
            endereco = request.POST['endereco'].strip(),
            observacao = request.POST['observacoes'].strip()
        )
        solicResgate.save()
    return render(request, "resgates.html")

def login(request):
    return render(request, "login.html")

def pessoas(request):
    if request.method == 'POST':
        cpf = request.POST['cpf'].strip()
        if not cpf_valido(cpf):
            context = {
                "errorMsg": "O CPF não é válido"
            }
            return render(request, "pessoas.html", context)
        
        pessoa = Pessoa (
            nome = request.POST['nome'].strip(),
            email = request.POST['email'].strip(),
            telefone = request.POST['telefone'].strip(),
            cpf = cpf,
            endereco = request.POST['endereco'].strip()
        )
        pessoa.save()
        return redirect('pessoas')
    else:
        pessoas = Pessoa.objects.all()

        context = {
            "pessoas": pessoas
        }

        return render(request, "pessoas.html", context)

def excluirPessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('pessoas')

def editarPessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        cpf = request.POST['cpf'].strip()
        if not cpf_valido(cpf):
            context = {
                "errorMsg": "O CPF não é válido"
            }
            return render(request, "pessoas.html", context)
    
        pessoa.nome = request.POST['nome'].strip()
        pessoa.cpf = cpf
        pessoa.email = request.POST['email'].strip()
        pessoa.telefone = request.POST['telefone'].strip()
        pessoa.endereco = request.POST['endereco'].strip()
        pessoa.save()
        return redirect('pessoas')
    else:
        pessoas = Pessoa.objects.all()
    
        context = {
            "pessoas": pessoas,
            "pessoa": pessoa
        }

        return render(request, "pessoas.html", context)

def relatorioDenuncias(request):
    denuncias = Denuncia.objects.all()

    context = {
        "denuncias": denuncias
    }
    return render(request, "relatorioDenuncias.html", context)

def relatorioResgates(request):
    resgates = SolicitacaoResgate.objects.all()

    context = {
        "solicitacoes" : resgates
    }
    return render(request, "relatorioResgates.html", context)