from datetime import datetime, timedelta

from django.views import generic
from django.shortcuts import redirect

from virtual_library.models import Book, RentOrder


class OrderDetailView(generic.DetailView):
    model = RentOrder
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['order'] = self.object
        return context


class OrderCreateView(generic.View):

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=self.kwargs['id'])
        user = self.request.user
        return_date = timedelta(days=30) + datetime.now()
        order = RentOrder.objects.create(book=book, user=user, return_date=return_date)
        order.book.status = 'on_rent'
        order.book.available_from = return_date
        order.book.save()
        return redirect('order_detail', pk=order.pk)
