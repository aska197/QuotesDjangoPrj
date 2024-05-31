from django.db import models
from django.utils import timezone

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255, null=True, blank=True)
    born_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class Quote(models.Model):
    tags = models.ManyToManyField('Tag', related_name='quotes')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    quote = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
