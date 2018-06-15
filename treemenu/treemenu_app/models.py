from django.db import models
from django.urls import reverse

# Create your models here.


class MenuItem(models.Model):

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='items'
    )
    real_url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    @property
    def url(self):
        if self.named_url:
            return reverse(self.named_url)
        else:
            return self.real_url

    def __str__(self):
        return self.title

