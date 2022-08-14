from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return  f'{self.name} ({self.id})'


class Book(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on_rent', 'On Rent'),
        ('sold', 'Sold'),
    )
    # book meta data
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField(blank=True)


    # product meta data
    owner = models.ForeignKey(UserModel, related_name='books', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
    rent = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    # time tracking data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.id})'
