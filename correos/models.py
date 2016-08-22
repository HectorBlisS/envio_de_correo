from django.db import models
from django.contrib.auth.models import User

class Suscriptor(models.Model):
	# user = models.OneToOneField(User, blank=True,null=True)
	email = models.EmailField()
	nombre = models.CharField(max_length=140)

