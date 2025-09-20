from django.db import models

class	Func(models.Model):
	nome = models.CharField(max_length=255, null=False, blank=False)
	sobrenome = models.CharField(max_length=255, null=False, blank=False)
	tempo = models.PositiveIntegerField(default=0, null=False, blank=False)
	bilhete = models.CharField(max_length=14, null=False, blank=False)
	salario = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)

	objetos = models.Manager()
