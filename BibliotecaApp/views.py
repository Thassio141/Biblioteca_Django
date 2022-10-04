from django.shortcuts import redirect ,render , HttpResponseRedirect
from .forms import AdicionarLivro, UsuarioForm
from .models import Livro
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


@staff_member_required
def add_show(request):
    if request.method == 'POST':
        fm = AdicionarLivro(request.POST)
        if fm.is_valid():
            titulo = fm.cleaned_data['titulo']
            slug = fm.cleaned_data['slug']
            autor = fm.cleaned_data['autor']
            descricao = fm.cleaned_data['descricao']
            genero = fm.cleaned_data['genero']
            qntd_livro = fm.cleaned_data['qntd_livro']
            data_lancamento = fm.cleaned_data['data_lancamento']
            reg = Livro(titulo=titulo, slug=slug, autor=autor, descricao=descricao, genero=genero, qntd_livro=qntd_livro,
                        data_lancamento=data_lancamento)
            reg.save()
            fm = AdicionarLivro()
    else:
        fm = AdicionarLivro()
    livros = Livro.objects.all()
    return render(request, 'BibliotecaApp/addElista.html', {'form': fm, 'livro': livros})

def update_data(request,id):
    if request.method == 'POST':
        pi = Livro.objects.get(pk=id)
        fm = AdicionarLivro(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')
    else:
        pi = Livro.objects.get(pk=id)
        fm = AdicionarLivro(instance=pi)

    return render(request, 'BibliotecaApp/atualizarLivro.html',{'form':fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = Livro.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


@login_required
def pag_user(request):
    livros = Livro.objects.all()
    return render(request, 'BibliotecaApp/pag_user.html', {'livro': livros})


class UsuarioCreate(CreateView):
    template_name = 'Usuarios/registrar.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = 'Cadastrar'

        return context




def alugar(request,id):
    aluguel = Livro.objects.get(id=id)
    aluguel.qntd_livro -= 1
    aluguel.save()
    return HttpResponseRedirect('/pag_user')
