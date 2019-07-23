from django.db import models
from user.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Favourite(models.Model):
    CATEGORY = [
        ('ppl', 'person'),
        ('pl', 'place'),
        ('fo', 'food')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=225, null=False, blank=False)
    description = models.CharField(max_length=300, null=False)
    ranking = models.IntegerField(null=False, blank=False)
    metadata = JSONField(null=True)
    Category = models.CharField(max_length=255, null=False, blank=False, choices=CATEGORY)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return
