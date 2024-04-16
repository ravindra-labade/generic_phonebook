from django.db import models


class Phonebook(models.Model):
    phone_no = models.IntegerField()
    person_name = models.CharField(max_length=20)
    person_city = models.CharField(max_length=20)
    choice = [('SIM', 'sim'), ('PHONE', 'phone')]
    storage_mode = models.CharField(max_length=10, choices=choice)

