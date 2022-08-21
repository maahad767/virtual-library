from django.shortcuts import render
from django.views import generic
from django.db.models.aggregates import Avg


from virtual_library.models import Book

class HomeView(generic.View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        qs = request.GET.get('q')
        books = Book.objects.all().annotate(avg_rating=Avg('rating__rating'))
        if qs:
            books = books.filter(title__icontains=qs)
        return render(request, self.template_name, {'books': books})
