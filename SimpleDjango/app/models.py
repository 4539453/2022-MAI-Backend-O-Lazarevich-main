import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy


def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))


class Film(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#uuidfield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(
        null=False,
        max_length=128,
        blank=False,
    )
    year = models.IntegerField(null=True, validators=[validate_positive])


class Director(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=128, blank=False)


class FilmDirector(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
