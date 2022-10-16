from django.urls import URLPattern, URLResolver, path

from .views import film, home

urlpatterns: list[URLPattern | URLResolver] = [
    path("web/", home, name="web"),
    path("api/", film, name="api"),
]
