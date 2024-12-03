from django.shortcuts import render, redirect
from .models import Jogo, Avaliacao
from .forms import JogoForm

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
            form.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm()
        
    return render(request, 'adicionar_jogo.html', {'form': form})