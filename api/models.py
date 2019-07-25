from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.validators import MinLengthValidator
from simple_history.models import HistoricalRecords
from datetime import timezone
# Create your models here.


class Category(models.Model):
    CATEGORIES = [
        ('ppl', 'person'),
        ('pl', 'place'),
        ('fod', 'food')
    ]
    name = models.CharField(max_length=225, unique=True, blank=False, null=True,
                            default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    audit_log = HistoricalRecords()

    def __str__(self):
        return self.name


class Favorite(models.Model):
    title = models.CharField(max_length=225, null=False, blank=False,default='')
    description = models.CharField(max_length=300, null=False,default='' , validators=[MinLengthValidator(10, 'description should '
                                                                                                  'not be less than '
                                                                                                  '10')])
    ranking = models.IntegerField(null=False,default='', blank=False)
    metadata = JSONField(null=True,
                         blank=True,
                         encoder=DjangoJSONEncoder,
                         help_text='types are TEXT=0, NUMBER=1, DATE=2, ENUM=3'
                         )
    category = models.ForeignKey('Category',default='', on_delete=models.CASCADE, related_name='favourites')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    audit_log = HistoricalRecords()

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.ranking, self.category)
