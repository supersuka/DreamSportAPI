from django.db import models
from django_softdelete.models import SoftDeleteModel

from .exercise import Exercise


class Approach(SoftDeleteModel):
    name = models.CharField(max_length=255, null=True, blank=True, default="Без названия")
    exercise = models.ForeignKey(Exercise, verbose_name="Упражнение", null=False, blank=True, on_delete=models.CASCADE)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    is_deleted = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return self.name