from django.contrib import admin
from django.urls import path

from apps.core.views import HomeView, healthcheck

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("api/health/", healthcheck, name="healthcheck"),
]