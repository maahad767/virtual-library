from django.db import models

from .user import User
from .category import Category


class Book(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on_rent', 'On Rent'),
        ('sold', 'Sold'),
    )
    # book meta data
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='media/book_covers', blank=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField(blank=True)

    # product meta data
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    rent = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    available_from = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.id})'

