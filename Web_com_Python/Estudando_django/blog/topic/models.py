from django.db import models

class Topic(models.Model):
	msg = models.CharField(max_length=200)
	data_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.msg} : {self.date_time}"
