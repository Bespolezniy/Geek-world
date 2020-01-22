from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImageStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded = models.DateTimeField(db_index = True, auto_now_add=True, verbose_name="Uploaded")
    image = models.ImageField(upload_to="imagestore/%Y/%m", verbose_name="Image")
    
    class Meta:
        ordering = ["user", "-uploaded"]
        verbose_name="image"
        verbose_name_plural="images"

    def delete(self, *args, **kwargs):
        self.image.delete(save = False)
        super(ImageStore, self).delete(*args, **kwargs)