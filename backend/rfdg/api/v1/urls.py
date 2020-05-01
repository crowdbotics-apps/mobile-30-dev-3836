from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SFffViewSet

router = DefaultRouter()
router.register("sfff", SFffViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
