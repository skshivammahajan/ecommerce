import random
import os
from django.db import models


def get_filenmae_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1000000)
    name, ext = get_filenmae_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)

    def features(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Products.objects
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 10, max_digits = 20)
    image = models.ImageField(upload_to = upload_image_path, null = True, blank = True)
    featured = models.BooleanField(default = False)

    objects = ProductManager()

    def __str__(self):
        return self.title

    # Python 2
    def __unicode__(self):
        return self.title