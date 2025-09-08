#!/usr/bin/env python3

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ["nome", "preco"]

	def clean_preco(self):
		preco = self.cleaned_data.get("preco")
		if preco <= 0:
			raise forms.ValidationsError("O preço deve ser maior que zero.")
		return preco
