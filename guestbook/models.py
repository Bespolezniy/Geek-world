from django.db import models

# Create your models here.

class GuestBook(models.Model):
    user = models.CharField(max_length=15, verbose_name="User")
    date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Published")
    content = models.TextField(verbose_name="Content")
    class Meta:
        ordering = ["-date"]
        verbose_name = "Guest book entry"
        verbose_name_plural = "Guest book entries"