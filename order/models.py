from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from book.models import Book
from user.models import User


class OrderStatus(models.TextChoices):
    c = 'cart'
    o = 'order'
    w = 'wishlist'


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    shipping_address = models.TextField(max_length=300)
    order_id = models.CharField(max_length=50)
    total_price = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=OrderStatus.choices, default=OrderStatus.c, max_length=10)

    def __str__(self):
        return str(self.id)


@receiver(pre_save, sender=Order)
def update_quantity(sender, instance, **kwargs):
    book = instance.book_id
    instance.total_price = book.price * instance.quantity
    if instance.quantity > book.quantity_now:
        raise Exception("The given quantity is not available")
    book.quantity_now -= instance.quantity
    if book.quantity_now < 0:
        raise Exception("Quantity is less than zero")
    book.save()
    return instance


