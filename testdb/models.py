from django.db import models

# Simply determine the database
class People(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
