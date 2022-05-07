from unittest import mock
from django.db import models
from Accounts.models import Account
# Create your models here.
import uuid


class Category(models.Model):

    Category_name = models.CharField(max_length=200)

    description_cat = models.TextField(max_length=500, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.Category_name


class Product(models.Model):

    owner = models.ForeignKey(Account, models.CASCADE)

    Product_name = models.CharField(max_length=200)

    description = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='photos/Product')

    Price = models.FloatField()

    Stock = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,

                          primary_key=True, editable=False)

    def __str__(self):

        return self.Product_name


class Review(models.Model):

    prouduct_review = models.ForeignKey(Product, on_delete=models.CASCADE)

    profiles = models.ForeignKey(Account, on_delete=models.CASCADE)

    review_title = models.CharField(max_length=200)

    review_body = models.TextField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,

                          primary_key=True, editable=False)

    class Meta:
        unique_together = ('prouduct_review', 'profiles',)

    def __str__(self):

        return self.review_title
