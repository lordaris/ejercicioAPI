from rest_framework import permissions, viewsets, status
from .serializers import (
    RutinaSerializer,
    DiaSerializer,
    EjercicioSerializer,
)
from .models import Rutina, Dia, Ejercicio
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(["GET"])
def rutina_list(request):
    rutinas = Rutina.objects.all()
    serializer = RutinaSerializer(rutinas, many=True)
    return Response(serializer.data)


class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer


class DiaViewSet(viewsets.ModelViewSet):
    queryset = Dia.objects.all()
    serializer_class = DiaSerializer


class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer


@api_view(["GET"])
def rutinas_json(request):
    rutinas = Rutina.objects.all()
    serializer = RutinaSerializer(rutinas, many=True)
    data = serializer.data
    with open("rutinas.json", "w") as f:
        json.dump(data, f)
    return JsonResponse(data, safe=False)
