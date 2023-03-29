from django.urls import include, path
from rest_framework import routers
from login import views
from rutinas import views as rutinas_views
from django.contrib import admin
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"rutinas", rutinas_views.RutinaViewSet)
router.register(r"dias", rutinas_views.DiaViewSet)
router.register(r"ejercicios", rutinas_views.EjercicioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("csrf-token/", views.csrf_token),
    path("admin/", admin.site.urls),
]
