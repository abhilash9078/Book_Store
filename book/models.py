from django.db import models


class Book(models.Model):
    """
    model class for book model
    """
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    quantity_now = models.PositiveIntegerField()
    ratings = models.PositiveIntegerField(default=4)
    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

