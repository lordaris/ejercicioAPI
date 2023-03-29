from django.db import models


class Rutina(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Dia(models.Model):
    rutina = models.ForeignKey(
        "Rutina", related_name="dias", on_delete=models.CASCADE, null=True
    )
    dia = models.CharField(max_length=100)
    enfoque = models.CharField(max_length=100)

    def __str__(self):
        return self.dia


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    repeticiones = models.CharField(max_length=100)
    cadencia = models.CharField(max_length=100)
    notas = models.TextField(null=True, blank=True)
    dia = models.ForeignKey(
        "Dia", related_name="ejercicios", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.nombre
