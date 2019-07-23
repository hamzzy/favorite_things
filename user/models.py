from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)
