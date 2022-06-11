import cloudinary.uploader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from matplotlib import pyplot as plt
import random

from portfolio.models import Cadeira, Elogio, Projeto, Competencia, PontuacaoQuizz, Noticia, ProjetoFinalDeCurso
from portfolio.forms import ElogiosForm, ProjetoForm, PessoaForm, CadeiraForm, TfcForm


def resolution_path(instance, filename):
    return f'users/{instance.id}/'


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def apresentacao_page_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/apresentacao.html', context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all(), 'projetosFinaisDeCurso': ProjetoFinalDeCurso.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def formprojetos_page_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/formProject.html', context)


@login_required
def view_editar_projeto(request, projeto_id):

    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editaProjeto.html', context)


def view_apagar_projeto(request, projeto_id):

    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


def formtfc_page_view(request):
    form = TfcForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/formTfc.html', context)


@login_required
def view_editar_tfc(request, tfc_id):
    tfc = ProjetoFinalDeCurso.objects.get(id=tfc_id)
    form = TfcForm(request.POST or None, instance=tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'tfc_id': tfc_id}
    return render(request, 'portfolio/editaTfc.html', context)


def view_apagar_tfc(request, tfc_id):
    tfc = ProjetoFinalDeCurso.objects.get(id=tfc_id)
    tfc.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


def formpessoa_page_view(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}

    return render(request, 'portfolio/fromPessoa.html', context)


def curso_page_view(request):
    context = {'cadeiras': Cadeira.objects.all(), 'range': range(1, 6)}
    return render(request, 'portfolio/curso.html', context)


def formcadeiras_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:curso'))

    context = {'form': form}

    return render(request, 'portfolio/formCadeira.html', context)


@login_required
def view_editar_cadeira(request, cadeira_id):

    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:curso'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editaCadeira.html', context)


def view_apagar_cadeira(request, cadeira_id):

    cadeira = Cadeira.objects.get(id=cadeira_id)
    cadeira.delete()
    return HttpResponseRedirect(reverse('portfolio:curso'))


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
    cloudinary.config(
        cloud_name="doqhqmtsl",
        api_key="154772819713293",
        api_secret="2jzlf0KAbEZ9QoICLZVJzSDKyv4"
    )
    nomes = []
    pontuacoes = []
    for resultado in PontuacaoQuizz.objects.all():
        nomes.append(resultado.nome)
        pontuacoes.append(resultado.pontuacao)
    nomes.reverse()
    pontuacoes.reverse()
    plt.barh(nomes, pontuacoes)
    plt.savefig('resultado.png', bbox_inches='tight')
    cloudinary.uploader.upload("resultado.png", public_id="portfolio/resultado")


def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados(request)
        return render(request, 'portfolio/programacaoWeb.html')

    return render(request, 'portfolio/formProgramacaoWeb.html')

