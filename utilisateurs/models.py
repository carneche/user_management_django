from django.db import models

class Users(models.Model):
    mat = models.CharField(unique=True, max_length=5)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    age = models.IntegerField()
    ville = models.CharField(max_length=100)
    pwd = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'
