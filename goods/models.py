from django.db import models
from categories.models import Category
from django.urls import reverse
from django_comments.moderation import CommentModerator, moderator

# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    description = models.TextField(verbose_name="Short description")
    content = models.TextField(verbose_name="Full description")
    price = models.FloatField(db_index=True, verbose_name="Price $")
    price_acc = models.FloatField(null=True, blank=True, verbose_name="Final price $")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="In stock")
    featured = models.BooleanField(default=False, db_index=True, verbose_name="Recomended")
    image = models.ImageField(upload_to="goods/list", verbose_name="Main image")

    def save(self, *args, **kwargs):
        try:
            this_record = Good.objects.get(pk = self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Good, self).delete(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("goods_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = "good"
        verbose_name_plural = "goods"

class GoodImage(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="goods/detail", verbose_name="Extra image")

    def save(self, *args, **kwargs):
        try:
            this_record = GoodImage.objects.get(pk = self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(GoodImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(GoodImage, self).delete(*args, **kwargs)
        
    class Meta:
        verbose_name = "image for good"
        verbose_name_plural = "images for good"

class GoodModerator(CommentModerator):
    email_notification = True
moderator.register(Good, GoodModerator)


