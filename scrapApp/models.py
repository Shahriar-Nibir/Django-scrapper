from django.db import models

# Create your models here.


class Post(models.Model):
    index = models.PositiveBigIntegerField(null=True, unique=True)
    title = models.CharField(max_length=300, null=True)
    link = models.URLField(max_length=300, null=True)
    comment = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title
