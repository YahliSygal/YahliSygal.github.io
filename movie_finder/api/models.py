
from django.db import models

class Watchlist(models.Model):
    user_id = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.movie_title} on {self.platform}'
