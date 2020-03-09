from django.db import models

# Create your models here.
class TodoItem(models.Model):
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
