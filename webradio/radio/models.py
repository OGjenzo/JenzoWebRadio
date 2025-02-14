from django.db import models

class Stream(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

