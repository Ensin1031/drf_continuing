from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from autoslug import AutoSlugField
from uuslug import uuslug


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


User = get_user_model()


class Car(models.Model):
    CAR_TYPE_CHOICES = (
        (1, 'Седан'),
        (2, 'Универсал'),
        (3, 'Джип'),
        (4, 'Микроавтобус'),
    )
    vin = models.CharField('Vin', max_length=100, unique=True, db_index=True)
    color = models.CharField('Цвет', max_length=100, blank=True)
    brand = models.CharField('Название', max_length=100)
    car_type = models.IntegerField('Тип кузова', choices=CAR_TYPE_CHOICES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='car_user')
    slug = AutoSlugField(
        'Url записи',
        max_length=50,
        db_index=True,
        unique=True,
        populate_from=instance_slug,
        slugify=slugify_value,
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.brand, instance=self)
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.brand + self.vin

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
