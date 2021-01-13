from django.db import models


class TimeStampedModel(models.Model):

    """ TimeStampedModel Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
