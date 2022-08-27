from django.shortcuts import render
from django.views import generic
from django.db.models.aggregates import Avg


from virtual_library.models import Book

class HomeView(generic.View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        query_string = request.GET.get('q')
        all_books = Book.objects.all().annotate(avg_rating=Avg('rating__rating'))
        filtered_books = self.filter_queryset(all_books, query_string)
        
        return render(request, self.template_name, {'books': filtered_books})

    def filter_queryset(queryset, query_string):
        if query_string:
            queryset = queryset.filter(title__icontains=query_string)
        return queryset
        