from django import forms

from .models import Character, Pericias, Post, RespostaPost, Aventura
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
# RespostaRespotaPost

class CharacterForm(forms.ModelForm):
    """docstring for CharacterForm."""
    class Meta:
        model = Character
        fields =   '__all__'
        exclude = ['author']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'classe': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'tamanho': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'idade': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'olhos': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'cabelo': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'pele': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'divindade': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'forca': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'constituicao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'destreza': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'inteligencia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'sabedoria': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'carisma': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'pontosDeVida': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'iniciativa': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'deslocamento': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
        }


class PericiasForm(forms.ModelForm):
    """docstring for CharacterForm."""
    class Meta:
        model = Pericias
        fields =   '__all__'
        exclude = ['character']
        widgets = {
         'acrobacia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'atletismo': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'blefe': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'diplomacia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'exploracao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'furtividade': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'historia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'intimidacao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'intuicao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'ladinagem': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'manha': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'natureza': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'percepcao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'religiao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'socorro': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'tolerancia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),

        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'categoria',)
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),

        # }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                Column('title', css_class='form-group col-md-4 col-md-offset-4'),
                Column('categoria', css_class='form-group col-md-2'),
                
                css_class='form-row'
            ),

            Row(
                Column('text', css_class='form-group col-md-6'),
                css_class='form-row'
                ),

            
            
        )
        self.helper.add_input(Submit('submit', 'Postar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))



class RespostaForm(forms.ModelForm):
    class Meta:
        model = RespostaPost
        fields = ('resposta', )


    def __init__(self, *args, **kwargs):
        super(RespostaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                Column('resposta', css_class='form-group col-md-4 col-md-offset-4'),
               
                
                css_class='form-row'
            ),


            
            
        )
        self.helper.add_input(Submit('submit', 'Postar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
  



class AventuraForm(forms.ModelForm):
    class Meta:
        model = Aventura
        fields = '__all__'
        exclude = ['author', 'create_date']

    def __init__(self, *args, **kwargs):
        super(AventuraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                
                Column('titulo', css_class='form-group col-md-4 col-md-offset-4'),
                Column('titulo', css_class='form-group col-md-4 col-md-offset-4'),
               
                
                css_class='form-row'
            ),


            
            
        )
        self.helper.add_input(Submit('submit', 'Postar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
 

class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))

