from django.db import models

class Produto(models.Model):
	nome = models.CharField(max_length=100)
	preco = models.DecimalField("Preço",max_digits=10, decimal_places=2)

	def	__str__(self):
		return f"{self.nome} - {self.preco} kz"

class Contacto(models.Model):
	nome = models.CharField(max_length=100)
	morada = models.CharField(max_length=200)
	tel = models.DecimalField(max_digits=12, decimal_places=2)

	def __str__(self):
		return f"{self.nome} - {self.morada} - {self.tel}"
