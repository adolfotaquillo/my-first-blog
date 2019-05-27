from django import forms  # importamos nuestros forms
from apps.crudjugadores.models import Jugador # importamos nuestro modelo jugador


# inicia la creacion de un Formulario:
class JugadorForm(forms.ModelForm):
   class Meta:
      model = Jugador #aplicamos al modelo jugador y acontinuacion los campos del formulario
      fields = [
         'id',
         'nombres',
         'apellidos',
         'fecha_nacimiento',
         'email',
         'deporte',
      ]

      labels = {
         'id': 'Identificacion',
         'nombres': 'Nombres',
         'apellidos': 'Apellidos',
         'fecha_nacimiento': 'Fecha de Nacimiento',
         'email': 'Correo Electronico',
         'deporte': 'Deporte',
      }
       
      # todos seran TextInput por que se ingresan datos, solo el deporte
      # sera un select
      widgets = {
         'id': forms.TextInput(attrs={'class':'form-control'}),
         'nombres': forms.TextInput(attrs={'class':'form-control'}),
         'apellidos': forms.TextInput(attrs={'class':'form-control'}),
         'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'deporte': forms.Select(attrs={'class':'form-control'}),
      }
