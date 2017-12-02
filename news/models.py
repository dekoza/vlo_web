from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField()
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ('important', 'pub_date')

    def __str__(self):
        return self.title
