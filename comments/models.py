from __future__ import unicode_literals
from django.db import models

class Comment(models.Model):
	commentor = models.CharField(max_length=32)
	comment = models.CharField(max_length=10000)
	time = models.CharField(max_length=32)

	def __str__(self):
		return self.commentor