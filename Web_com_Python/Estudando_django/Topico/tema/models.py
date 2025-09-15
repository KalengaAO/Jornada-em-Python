from django.db import models

class Tema(models.Model):
	topico = models.CharField(max_length=200)
	data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.topico} :  {self.data}"

class Subtema(models.Model):
	topico = models.ForeignKey(Tema, on_delete=models.CASCADE)
	subtema = models.TextField()
	data = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "SubTema"

	def __str__(self):
		return f"{self.topico} : {self.subtema[:20]}... :{self.data}"
