from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='BrandName')
    description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
