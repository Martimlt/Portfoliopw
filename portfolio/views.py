from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from matplotlib import pyplot as plt

from portfolio.models import Cadeira, Elogio, Projeto, Competencia, PontuacaoQuizz, Noticia
from portfolio.forms import ElogiosForm, ProjetoForm


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def apresentacao_page_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/apresentacao.html',context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def formprojetos_page_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/formProject.html', context)


def curso_page_view(request):
    context = {'cadeiras': Cadeira.objects.all(), 'range': range(1, 6)}
    return render(request, 'portfolio/curso.html', context)


def elogios_page_view(request):
    context = {'elogios': Elogio.objects.all()}
    return render(request, 'portfolio/elogios.html', context)


def formElogios_page_view(request):
    form = ElogiosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:elogios'))

    context = {'form': form}

    return render(request, 'portfolio/formElogios.html', context)


def programacaoWeb_page_view(request):
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'portfolio/programacaoWeb.html', context)


def formPW_page_view(request):
    return render(request, 'portfolio/formProgramacaoWeb.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Login Inválido.'
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
        "message": "Logged out."
    })


def pontuacao_quizz(request):
    resultado = 0
    if request.POST["linha"] == "!DOCTYPE html":
        resultado += 1
    if request.POST["resposta"] == "question":
        resultado += 1
    if request.POST["estilo"] == "css":
        resultado += 1
    if request.POST["beneficios"] == "Restrito":
        resultado += 1
    if request.POST["framework"] == "Python":
        resultado += 1
    return resultado


def desenha_grafico_resultados(request):
    nomes = []
    pontuacoes = []
    for resultado in PontuacaoQuizz.objects.all():
        nomes.append(resultado.nome)
        pontuacoes.append(resultado.pontuacao)
    nomes.reverse()
    pontuacoes.reverse()
    plt.barh(nomes, pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/resultado.png', bbox_inches='tight')


def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados(request)
        return render(request, 'portfolio/ProgramacaoWeb.html')

    return render(request, 'portfolio/formProgramacaoWeb.html')

