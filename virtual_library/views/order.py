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
        order = self.create_new_order()
        self.update_order_info(order)
        return redirect('order_detail', pk=order.pk)

    def create_new_order(self):
        book = Book.objects.get(id=self.kwargs['id'])
        user = self.request.user
        return_date = self.get_return_date()
        order = RentOrder.objects.create(book=book, user=user, return_date=return_date)
        return order
    
    def update_order_info(self, order):
        order.book.status = 'on_rent'
        order.book.available_from = self.get_return_date()
        order.book.save()


    def get_return_date(self):
        return timedelta(days=30) + datetime.now()
