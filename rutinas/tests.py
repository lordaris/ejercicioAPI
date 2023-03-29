from django.test import TestCase

# Create your tests here.

data = {
    "nombre": "Rutina de prueba",
    "dias": [
        {
            "dia": "Día 1",
            "enfoque": "Piernas",
            "ejercicios": [
                {
                    "nombre": "Sentadillas",
                    "series": "3",
                    "repeticiones": "10",
                    "cadencia": "2-1-2",
                    "notas": "Mantener la espalda recta",
                },
                {
                    "nombre": "Peso muerto",
                    "series": "3",
                    "repeticiones": "8",
                    "cadencia": "3-1-3",
                    "notas": "Usar cinturón de levantamiento",
                },
            ],
        }
    ],
}

from rutinas.serializers import RutinaSerializer

serializer = RutinaSerializer(data=data)
serializer.is_valid()
serializer.save()
