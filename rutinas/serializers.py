from rest_framework import serializers
from .models import Ejercicio, Dia, Rutina


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ("id", "nombre", "series", "repeticiones", "cadencia", "notas")


class DiaSerializer(serializers.ModelSerializer):
    ejercicios = EjercicioSerializer(many=True)

    class Meta:
        model = Dia
        fields = ("id", "dia", "enfoque", "ejercicios")


class RutinaSerializer(serializers.ModelSerializer):
    dias = DiaSerializer(many=True)

    class Meta:
        model = Rutina
        fields = ("id", "nombre", "dias")

    def create(self, validated_data):
        dias_data = validated_data.pop("dias")
        rutina = Rutina.objects.create(**validated_data)
        for dia_data in dias_data:
            ejercicios_data = dia_data.pop("ejercicios")
            dia = Dia.objects.create(rutina=rutina, **dia_data)
            for ejercicio_data in ejercicios_data:
                Ejercicio.objects.create(dia=dia, **ejercicio_data)
        return rutina
