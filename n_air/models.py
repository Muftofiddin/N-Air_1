from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)



