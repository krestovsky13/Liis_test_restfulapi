from django.db import models
from django.conf import settings
import datetime


class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    slug = models.SlugField()
    content = models.TextField(null=False)
    created_at = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
