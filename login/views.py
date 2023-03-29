from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from login.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.response import Response


@api_view(["GET"])
def csrf_token(request):
    csrf = get_token(request)
    response = JsonResponse({"csrfToken": csrf})
    response["X-CSRFToken"] = csrf
    return response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
