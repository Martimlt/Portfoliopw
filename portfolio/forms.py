from django import forms
from django.forms import ModelForm
from .models import Elogio, Projeto, Pessoa, Cadeira, ProjetoFinalDeCurso


class ElogiosForm(ModelForm):
    class Meta:
        model = Elogio
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'primeiroNome': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o seu primeiro nome'}),
            'ultimoNome': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o seu último nome'}),
            'trabalho': forms.Textarea(
                attrs={'class': 'linebreakTextArea1', 'placeholder': 'Insira o(s) trabalho(s) que fizemos juntos'}),
            'elogio': forms.Textarea(attrs={'class': 'linebreakTextArea2', 'placeholder': 'Insira o elogio'}),
            'data': forms.DateField()
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'primeiroNome': 'Primeiro Nome',
            'ultimoNome': 'Último nome',
            'trabalho': 'Que trabalhos fizemos juntos?',
            'elogio': 'Elogio',
            'data': 'Data'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o título'}),
            'descricao': forms.Textarea(attrs={'class': 'linebreakTextArea2', 'placeholder': 'Insira a descrição'}),
            'linkGit': forms.URLInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o link'}),
            'ano': forms.NumberInput(attrs={'class': 'spaceform', 'placeholder': 'Insira o ano'}),
            'tecnologia': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira a tecnologia'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'linkGit': 'LinkGit',
            'cadeira': 'Cadeira',
            'ano': 'Ano em que realizei o projeto',
            'imagem': 'Imagem representativa',
            'tecnologia': 'Tecnologia utilizada',
            'participante': 'Colega com quem realizei o projeto',
            'competencia': 'Competencia adquirida',
            'left': 'Fotografia à Esquerda',
            'right': 'Fotografia à Direita',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'primeiroNome': forms.TextInput(attrs={'placeholder': 'Insira o primeiro nome'}),
            'ultimoNome': forms.TextInput(attrs={'placeholder': 'Insira o segundo nome'}),
            'linkedin': forms.URLInput(attrs={'placeholder': 'Insira o link'}),
            'outroLink': forms.URLInput(attrs={'placeholder': 'Link Lusófona ou Heroku'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'primeiroNome': 'Primeiro Nome',
            'ultimoNome': 'Último Nome',
            'linkedin': 'Linkedin',
            'outroLink': 'Página Lusófona ou Heroku',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o nome da cadeira'}),
            'descricao': forms.Textarea(attrs={'class': 'linebreakTextArea2', 'placeholder': 'Insira a descrição'}),
            'ano': forms.NumberInput(attrs={'class': 'spaceform','placeholder': 'Insira o ano'}),
            'semestre': forms.NumberInput(attrs={'class': 'spaceform','placeholder': 'Insira o semestre'}),
            'ects': forms.NumberInput(attrs={'class': 'spaceform', 'placeholder': 'Insira os Ects'}),
            'ranking': forms.NumberInput(attrs={'class': 'spaceform', 'placeholder': 'Insira o ranking'}),
            'linklusofona': forms.URLInput(attrs={'class': 'linebreak', 'placeholder': 'Insira a Página da Lusófona'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome cadeira',
            'descricao': 'Descrição',
            'professorAuxiliar': 'Professor Auxiliar',
            'linklusofona': 'Link site lusófona',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }


class TfcForm(ModelForm):
    class Meta:
        model = ProjetoFinalDeCurso
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o titulo'}),
            'ano': forms.NumberInput(attrs={'class': 'spaceform', 'placeholder': 'Insira o ano'}),
            'resumo': forms.Textarea(attrs={'class': 'linebreakTextArea2', 'placeholder': 'Insira o resumo'}),
            'relatorio': forms.URLInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o link do relatório'}),
            'github': forms.URLInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o link do Github'}),
            'video': forms.URLInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o link do vídeo'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Titulo TFC',
            'orientador': 'Professor Orientador',
            'imagem': 'Imagem Projeto',
            'relatorio': 'Relatório Projeto',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }
