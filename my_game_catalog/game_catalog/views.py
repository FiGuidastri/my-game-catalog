from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Jogo, Avaliacao
from .forms import JogoForm, AvaliacaoForm, RegistroUsuarioForm

def jogo_list(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogo_list.html', {'jogos': jogos})

def jogo_detalhes(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    avaliacoes = Avaliacao.objects.filter(jogo=jogo)
    return render(request, 'jogo_detalhes.html', {'jogo': jogo, 'avaliacoes': avaliacoes})

def adicionar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            jogo = form.save()

            # Verifica se o status do jogo é "zerado"
            if jogo.status == "zerado":
                # Criar avaliação automaticamente (ajustar nota e comentário conforme necessário)
                usuario = request.user  # Aqui o usuário logado será o responsável pela avaliação
                avaliacao = Avaliacao.objects.create(
                    usuario=usuario,
                    jogo=jogo,
                    nota=5,  # Atribuindo uma nota fixa, pode ser ajustada conforme a lógica
                    comentario="Avaliação automática - Status zerado"  # Comentário fixo ou personalizado
                )
                avaliacao.save()

            # Redireciona para a página de sucesso ou exibe o jogo
            return redirect(reverse('home'))  # Corrigido para 'home' em vez de 'home.html'

    else:
        form = JogoForm()

    return render(request, 'adicionar_jogo.html', {'form': form})

@login_required
def home(request):
    jogos = Jogo.objects.all()
    return render(request, 'home.html', {'jogos' : jogos})

@login_required
def editar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)

    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('status') == 'zerado':
                return redirect('avaliar_jogo', jogo_id=jogo.id)  # Redireciona para avaliação
            return redirect('home')  # Redireciona para a página inicial após edição
    else:
        form = JogoForm(instance=jogo)

    return render(request, 'editar_jogo.html', {'form': form, 'jogo': jogo})

@login_required
def avaliar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.jogo = jogo
            avaliacao.usuario = request.user  # Associando o usuário logado à avaliação
            avaliacao.save()
            return redirect(reverse('home'))  # Ou para outra página desejada
    else:
        form = AvaliacaoForm()

    return render(request, 'avaliar_jogo.html', {'form': form, 'jogo': jogo})


def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Após o registro, redireciona para a página de login
    else:
        form = UserCreationForm()

    return render(request, 'registro.html', {'form': form})