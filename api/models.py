from auditlog.models import AuditlogHistoryField
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.validators import MinLengthValidator


# Create your models here.


class Category(models.Model):
    CATEGORIES = [
        ('ppl', 'person'),
        ('pl', 'place'),
        ('fod', 'food')
    ]
    name = models.CharField(max_length=225, null=False, blank=False, choices=CATEGORIES, unique=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    title = models.CharField(max_length=225, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, validators=[MinLengthValidator(10, 'description should '
                                                                                                  'not be less than '
                                                                                                  '10')])
    ranking = models.IntegerField(null=False, blank=False)
    metadata = JSONField(null=True)
    category = models.ForeignKey(Category, related_name='favourites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    audit_log = AuditlogHistoryField()

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.ranking, self.category)
