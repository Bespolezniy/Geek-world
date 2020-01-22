from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name="Name")
    order = models.PositiveSmallIntegerField(default=0, unique=True, verbose_name="Order number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "category"
        verbose_name_plural = "categories"
    
