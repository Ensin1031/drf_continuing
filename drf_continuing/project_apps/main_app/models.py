from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from uuslug import uuslug


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


"""
config autoslug in models

class Category(models.Model):
    title = models.CharField('Название категории', max_length=50, db_index=True)
    slug = AutoSlugField(
        'Url записи',
        max_length=50,
        db_index=True,
        unique=True,
        populate_from=instance_slug,
        slugify=slugify_value,
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории(й)'
        ordering = ('title',)


"""