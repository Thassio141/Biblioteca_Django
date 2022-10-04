
from turtle import width
from django import forms
from .models import Livro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput


class AdicionarLivro(forms.ModelForm):
    imagem = forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model = Livro
        fields = ['titulo', 'slug', 'imagem', 'autor', 'descricao', 'genero', 'qntd_livro', 'data_lancamento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'qntd_livro': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_lancamento': forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'})
        }


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User 
        fields = ['username', 'email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

'''
class LivroPhotoForm(forms.ModelForm):
    required_css_class = 'required'
    photo = forms.ImageField(required=False)

    class Meta:
        model = Livro
        fields = ['photo','titulo', 'slug', 'autor', 'descricao', 'genero', 'qntd_livro', 'data_lancamento']

    def __init__(self,*args,**kwargs):
        super(LivroPhotoForm, self).__init__(*args,**kwargs)
        for field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = None
        '''