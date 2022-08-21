from django.views import generic


class OrderView(generic.TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context