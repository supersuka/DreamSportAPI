from django.contrib.auth.models import User
from django.db import models
from django_softdelete.models import SoftDeleteModel


class ExercisePhotos(SoftDeleteModel):
    name = models.CharField(max_length=255, verbose_name="Название", default="(Без имени)", blank=True)
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение", upload_to='files/photos/')
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    is_deleted = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return self.name
