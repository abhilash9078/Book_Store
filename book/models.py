from django.db import models
import datetime


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    quantity_now = models.IntegerField()
    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.book_name
