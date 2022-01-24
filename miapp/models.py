from django.db import models

# Create your models here.
class Document(models.Model):
    DOCUMENT_TYPE = (
        (1, 'TI', 'Tarjeta Identidad'),
        (2, 'CC', 'Cedula Ciudadania'),
        (3, 'PT', 'Pasaporte')
    )
    id_document = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=2, choices=DOCUMENT_TYPE)

class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    id_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)