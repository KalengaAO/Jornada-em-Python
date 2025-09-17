from django import forms
from .models import Tema, Subtema

class	FormTopico(forms.ModelForm):
	class Meta:
		model = Tema
		fields = ["topico"]

class	FormSubtema(forms.ModelForm):
	class Meta:
		model = Subtema
		fields = ["subtema"]
		widgets = {'subtema': forms.Textarea(attrs={'cols':50, 'rows':'5', 'placeholder':'digite aqui'})}

class	EditarForm(forms.ModelForm):
	class Meta:
		model = Subtema
		fields = ['subtema']
		widgets = {'subtema': forms.Textarea(attrs={'cols':'50', 'rows':'5', 'placeholder':'edite aqui'})}
