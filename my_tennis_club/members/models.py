from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    direction = models.CharField(null=True)
    tipe_sexo = models.CharField(null=True)
    number_document = models.IntegerField(null=True)
