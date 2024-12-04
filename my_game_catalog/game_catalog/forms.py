from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Jogo, Avaliacao

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
    
class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': 1}),
            'comentario': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nota': 'Nota (0 a 10)',
            'comentario': 'Comentário',
        }
        
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']