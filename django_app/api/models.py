from django.db import models

class ScrapedData(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title
