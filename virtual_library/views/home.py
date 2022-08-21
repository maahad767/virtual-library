from django.shortcuts import render
from django.views import generic
from django.db.models.aggregates import Avg


from virtual_library.models import Book

class HomeView(generic.View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all().annotate(avg_rating=Avg('rating__rating'))
        return render(request, self.template_name, {'books': books})
