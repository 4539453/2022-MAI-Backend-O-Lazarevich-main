from app.models import Director, Film
from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year")
    # list_filter = ("year",)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
