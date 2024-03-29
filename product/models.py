import uuid

from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.URLField(blank=True)
    description = models.TextField(null=True,blank=True, default='N/A')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=250)
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title