from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ('titulo', 'genero', 'plataforma', 'ano_lancamento', 'status')
        
        # Personalizando os widgets (opcional)
    titulo = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Jogo'}))
    genero = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gênero'}))
    plataforma = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plataforma'}))
    ano_lancamento = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Lançamento'}))
    status = forms.ChoiceField(choices=Jogo.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))