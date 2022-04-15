from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from django.utils.timezone import now
from rest_framework import serializers


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset


class Comment(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )


    comment = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    objects = CommentManager()

    class MPTTMeta:
        order_insertion_by=['created']

    class Meta:
        ordering = ['tree_id', 'lft']
