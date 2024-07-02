from django.db import models
from django.utils import timezone
from djongo import models as djongo_models
from uuid import uuid4
from django.db import models

class Author(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    fullname = djongo_models.CharField(max_length=255)
    born_date = djongo_models.CharField(max_length=255, null=True, blank=True)
    born_location = djongo_models.CharField(max_length=255, null=True, blank=True)
    description = djongo_models.TextField(null=True, blank=True)
    created_at = djongo_models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'authors'

class Quote(djongo_models.Model):  # Changed to djongo_models.Model for consistency
    tags = djongo_models.ManyToManyField('Tag', related_name='quotes')
    author = djongo_models.ForeignKey(Author, on_delete=djongo_models.CASCADE, related_name='quotes')
    quote = djongo_models.TextField()
    created_at = djongo_models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'quotes'

class Tag(djongo_models.Model):  # Changed to djongo_models.Model for consistency
    name = djongo_models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'


    
