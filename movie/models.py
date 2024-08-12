from django.db import models
from django.urls import reverse


# Create your models here.

class Movie(models.Model):
    genre = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    poster = models.ImageField(upload_to='movies/%y/%m/%d', blank=True)
    release_date = models.DateTimeField()
    plot = models.CharField(max_length=500)
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    running_time = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:movie_detail', args=[self.id])
