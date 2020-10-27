from django.db import models

class Account(models.Model):
	login = models.CharField(max_length=50)
	passwd = models.CharField(max_length=50)

	def __str__(self):
		return (self.login) + '|' + (self.passwd)