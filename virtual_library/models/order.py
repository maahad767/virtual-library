from django.db import models


class RentOrder(models.Model):
    user = models.ForeignKey('virtual_library.User', on_delete=models.CASCADE)
    book = models.ForeignKey('virtual_library.Book', on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.book}'

    class Meta:
        verbose_name = 'Rent Order'
        verbose_name_plural = 'Rent Orders'
