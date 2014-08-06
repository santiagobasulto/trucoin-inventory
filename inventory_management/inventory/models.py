from django.db import models

from django_extensions.db.models import TimeStampedModel

__all__ = ['Product']


class Product(TimeStampedModel):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    inventory_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} ({} items left)".format(self.name, self.inventory_count)