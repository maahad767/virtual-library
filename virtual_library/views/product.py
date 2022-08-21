from django.views import generic

from virtual_library.models import Book

class ProductDetailView(generic.DetailView):
    model = Book
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
