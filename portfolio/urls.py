#  hello/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('formprojetos', views.formprojetos_page_view, name='formprojetos'),
    path('editarProjeto/<int:projeto_id>', views.view_editar_projeto, name='editarProjeto'),
    path('apagarProjeto/<int:projeto_id>', views.view_apagar_projeto, name='apagarProjeto'),
    path('tfc', views.tfc_page_view, name='tfc'),
    path('formtfc', views.formtfc_page_view, name='formtfc'),
    path('editarTfc/<int:tfc_id>', views.view_editar_tfc, name='editarTfc'),
    path('apagarTfc/<int:tfc_id>', views.view_apagar_tfc, name='apagarTfc'),
    path('formpessoa', views.formpessoa_page_view, name='formpessoa'),
    path('curso', views.curso_page_view, name='curso'),
    path('editarCadeira/<int:cadeira_id>', views.view_editar_cadeira, name='editarCadeira'),
    path('apagarCadeira/<int:cadeira_id>', views.view_apagar_cadeira, name='apagarCadeira'),
    path('formcadeiras', views.formcadeiras_page_view, name='formcadeiras'),
    path('elogios', views.elogios_page_view, name='elogios'),
    path('formElogios', views.formElogios_page_view, name='formElogios'),
    path('programacaoWeb', views.programacaoWeb_page_view, name='programacaoWeb'),
    path('quizz', views.quizz_view, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('contacto', views.contacto_page_view, name='contacto'),
]
