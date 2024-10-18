from django.db import models

class ScrapedData(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title
