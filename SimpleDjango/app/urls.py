from django.urls import URLPattern, URLResolver, path

from .views import book, home

urlpatterns: list[URLPattern | URLResolver] = [
    path("web/", home, name="web"),
    path("api/", book, name="api"),
]
