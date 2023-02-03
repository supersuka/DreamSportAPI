from django.db import models
from django_softdelete.models import SoftDeleteModel

from .approach import Approach


class Trains(SoftDeleteModel):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(null=True, verbose_name="Описание")
    monday = models.BooleanField(default=False, verbose_name="Понедельник")
    thuesday = models.BooleanField(default=False, verbose_name="Вторник")
    wednsday = models.BooleanField(default=False, verbose_name="Среда")
    thursday = models.BooleanField(default=False, verbose_name="Четверг")
    friday = models.BooleanField(default=False, verbose_name="Пятница")
    saturday = models.BooleanField(default=False, verbose_name="Суббота")
    sunday = models.BooleanField(default=False, verbose_name="Воскресенье")
    approach = models.ManyToManyField(Approach, null=True, blank=True, verbose_name="Подход/Упражнение")
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    is_deleted = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return self.name