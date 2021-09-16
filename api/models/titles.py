from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models

from .categories import Category
from .genres import Genre


class Title(models.Model):
    name = models.CharField(
        max_length=300,
        blank=False,
        verbose_name='Name',
    )
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.now().year)],
        db_index=True,
        verbose_name='Year',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        # null=True,
        verbose_name='Genre',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Category',
    )
