from django import forms
from django.forms import ModelForm
from .models import Elogio, Projeto


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
            'linkGit': forms.URLInput(attrs={'class': 'linebreak','placeholder': 'Insira o link'}),
            'cadeira': forms.TextInput(attrs={'class': 'spaceform','placeholder': 'Insira a cadeira'}),
            'ano': forms.NumberInput(attrs={'class': 'spaceform','placeholder': 'Insira o ano'}),
            'imagem': forms.FileInput(attrs={'class': 'spaceform','placeholder': 'Insira o seu primeiro nome'}),
            'tecnologia': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira a tecnologia'}),
            'participante': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira o colega'}),
            'competencia': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Insira a competencia'}),
            'left': forms.TextInput(attrs={'class': 'spaceform'}),
            'right': forms.TextInput(attrs={'class': 'spaceform'}),
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
