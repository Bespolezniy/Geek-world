from django.db import models
from datetime import datetime

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100, unique_for_date = "date", verbose_name = "New title")
    description = models.TextField(verbose_name="Short content")
    content = models.TextField(verbose_name="All information")
    date = models.DateField(default=datetime.now(), db_index=True, verbose_name="Published")
    
    class Meta:
        ordering = ["-date"]
        verbose_name = "new"
        verbose_name_plural = "news"


