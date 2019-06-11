from django import forms

from .models import Quiz, Pergunta, Resposta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ['titulo', 'descricao', 'numPerguntas']
		def __init__(self, *args, **kwargs):
			super(QuizForm, self).__init__(*args, **kwargs)
			self.helper = FormHelper(self)
			self.helper.form_method = 'POST'
			self.helper.layout = Layout(
			Row(

			Column('titulo', css_class='form-group col-md-3 col-md-offset-3'),
			Column('descricao', css_class='form-group col-md-3 col-md-offset-3'),   
			Column('numPerguntas', css_class='form-group col-md-3'),   
			css_class='form-row'
			),

			)
			self.helper.add_input(Submit('submit', 'Postar'))
			self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))



class PerguntasForm(forms.ModelForm):
	class Meta:
		model = Pergunta
		fields = ['pergunta']
		exclude = ['quiz',]
		widgets = {
            'pergunta': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class RespostaForm(forms.ModelForm):
	class Meta:
		model = Resposta
		fields = ['resposta']
		widgets = {
            'resposta': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }








