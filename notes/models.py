from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор записи')

    text = models.TextField(verbose_name='Текс записи', null=False, blank=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=False, null=False)

    created_at = models.DateTimeField(verbose_name='Дата создания', null=False, default=datetime.now)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', null=False, default=datetime.now)
    closed_at = models.DateTimeField(verbose_name='Дата закрытия', null=True)

    done = models.BooleanField(verbose_name='Выполнено ли', default=False)

    author = models.ForeignKey(null=True, to=User, on_delete=models.DO_NOTHING, verbose_name='Автор')
