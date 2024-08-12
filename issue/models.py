from django.db import models

# Create your models here.
from django.urls import reverse


class Issue(models.Model):
    issue_title = models.CharField(max_length=200, db_index=True)
    issue_date = models.DateTimeField()
    issue_content = models.CharField(max_length=200, db_index=True)
    issue_poster = models.ImageField(upload_to='issues/%y/%m/%d', blank=True)

    def __str__(self):
        return self.issue_title

    def get_absolute_url(self):
        return reverse('issue:issue_detail', args=[self.id])
