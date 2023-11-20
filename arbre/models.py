from django.db import models


# Create your models here.

class Personne(models.Model):
    SEXE_CHOICES = [("homme", "homme"), ("femme", "femme")]

    user_name = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sexe = models.CharField(max_length=40, choices=SEXE_CHOICES, blank=True)
    pere = models.IntegerField(blank=True, null=True)
    mere = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user_name
