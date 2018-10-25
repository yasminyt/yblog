from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=128, default="")
    description = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import  reverse
        return reverse('view_category', kwargs={'sulg': self.slug})

    class Meta:
        verbose_name_plural = "categories"
