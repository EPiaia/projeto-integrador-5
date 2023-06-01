"""
URL configuration for pi5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('adocao/', views.adocao, name='adocao'),
    path('adotar/', views.adotar, name='adotar'),
    path('animais/', views.animais, name='animais'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('denuncias/', views.denuncias, name='denuncias'),
    path('login/', views.login, name='login'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('racas/', views.racas, name='racas'),
    path('relatorioDenuncias/', views.relatorioDenuncias, name='relatorioDenuncias'),
    path('relatorioResgates/', views.relatorioResgates, name='relatorioResgates'),
    path('resgates/', views.resgates, name='resgates'),
    path('excluir_raca/<int:id>', views.excluirRaca, name="excluir_raca"),
    path('editar_raca/<int:id>', views.editarRaca, name="editar_raca"),
    path('excluir_animal/<int:id>', views.excluirAnimal, name="excluir_animal"),
    path('editar_animal/<int:id>', views.editarAnimal, name="editar_animal")
]
