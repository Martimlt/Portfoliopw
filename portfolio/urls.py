#  hello/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('formprojetos', views.formprojetos_page_view, name='formprojetos'),
    path('curso', views.curso_page_view, name='curso'),
    path('elogios', views.elogios_page_view, name='elogios'),
    path('formElogios', views.formElogios_page_view, name='formElogios'),
    path('programacaoWeb', views.programacaoWeb_page_view, name='programacaoWeb'),
    path('quizz', views.quizz_view, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('contacto', views.contacto_page_view, name='contacto'),
]
