from django.db import models
from django.utils.text import slugify

from regis.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    key = models.SlugField(max_length=128, blank=True)
    is_menu = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Products(models.Model):
    product_id = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.CharField(max_length=128, blank=False, null=False, default="MDF")
    color = models.CharField(max_length=128)
    img = models.ImageField()

    def __str__(self):
        return self.product_id

class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    def __str__(self):
        return self.name



class Basket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        return super(Basket, self).save(*args, **kwargs)

    def __str__(self):
        return self.product


class Likes(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def res(self):
        return {
            "product_id": self.product.id,
            "user": self.user.id,
            "like": self.like,
            "dislike": self.dislike,

        }






