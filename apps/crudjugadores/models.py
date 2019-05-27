# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Deporte(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return "{1}".format(self.id,self.nombre)
        #return '{}'.format(self.nombre)
        

class Jugador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    deporte = models.ForeignKey(Deporte, null=True,blank=True, on_delete= models.CASCADE)

    def NombreCompleto(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.id, self.nombres , self.apellidos)

    def __str__(self):
        return self.NombreCompleto()
