from django.views import generic
from django.urls import reverse_lazy

from virtual_library.models import Book, Category

class ProductDetailView(generic.DetailView):
    model = Book
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['book'] = self.object
        return context


class ProductCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'rent', 'cover_photo', 'category', 'published_date']
    template_name = 'product_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)