from django.shortcuts import render,redirect,HttpResponse
from .models import Curso
from .forms import CursoForm


def contato(request): # Pagina contato
    return render(request, 'cursos/contato.html')

def cursos(request):
    dados = {
        'dados': Curso.objects.all() # Vai extrair as informações da tabela Curso no banco de dados
    }
    return render(request, 'cursos/cursos.html', context=dados)

def detalhe(request, id_curso):
    dados = {
        'dados': Curso.objects.get(pk=id_curso)
    }
    return render(request, 'cursos/detalhe.html', dados)

def criar(request):
    if request.method == 'POST':
        curso_form = CursoForm(request.POST)
        if curso_form.is_valid():
            curso_form.save()
        return redirect('cursos')
    else:   
        curso_form = CursoForm()
        formulario = {
            'formulario': curso_form
        }
        return render(request, 'cursos/novo_curso.html', context=formulario)

def editar(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    # novo_curso/1 -> GET
    if request.method == 'GET':
        formulario = CursoForm(instance=curso)
        return render(request, 'cursos/novo_curso.html',{'formulario': formulario})
    # caso requisição seja POST
    else:
        formulario = CursoForm(request.POST, instance=curso)
        if formulario.is_valid():
            formulario.save()
        return redirect('cursos')

def excluir(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')
    return render(request, 'cursos/confirmar_exclusao.html', {'item': curso})

