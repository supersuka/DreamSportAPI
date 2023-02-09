from django.contrib.auth.models import User
from django.db import models
from django_softdelete.models import SoftDeleteModel

from .exercise_photos import ExercisePhotos


class Exercise(SoftDeleteModel):
    name = models.CharField(max_length=255, verbose_name="Название")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    description = models.TextField(null=True, verbose_name="Описание")
    valueType = models.SmallIntegerField(default=1, verbose_name="Мера измерения (кг, см)")
    countType = models.SmallIntegerField(default=1, verbose_name="Мера количества (шт, время(мм:сс))")
    considerOwnWeight = models.BooleanField(default=False, verbose_name="Учитывать собственный вес")
    video = models.FileField(upload_to='files/videos/', verbose_name="Видео файл", null=True, blank=True)
    photos = models.ManyToManyField(ExercisePhotos, null=True, blank=True, verbose_name="Изображения")
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    is_deleted = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return self.name