from django.conf import settings
from django.db import models
from django.db import models
from datetime import datetime


class Dog(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(default=datetime.now)
    owner =  models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            )

    # def __str__(self):
    #     return "{} <> {}".format(self.name, self.date_of_birth)
