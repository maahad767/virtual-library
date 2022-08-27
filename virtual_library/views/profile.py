from django.views import generic
from django.urls import reverse_lazy

from virtual_library.models import User

class ProfileView(generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ProfileUpdateView(generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'photo', 'phone', 'address']
    template_name = 'profile_update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
        