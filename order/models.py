from django.db import models
from book.models import Book
from user.models import User


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False)
    shipping_address = models.TextField(max_length=300, null=False)
    order_id = models.CharField(max_length=50)
    total_price = models.IntegerField(null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(choices=)

    def __str__(self):
        return str(self.id)

