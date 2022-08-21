from django.db import models

from .user import User
from .book import Book

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)
    comment = models.TextField()
    
    class Meta: 
        unique_together = ('book', 'user')
