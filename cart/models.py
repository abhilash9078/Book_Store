from django.db import models
from book.models import Book
from user.models import User


class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created_dt = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.id
