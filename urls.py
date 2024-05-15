from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("django_tailwind_app/", include("django_tailwind_app.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]