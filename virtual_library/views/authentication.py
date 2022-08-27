from django.shortcuts import render, redirect
from django.contrib.auth import views as authviews
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from virtual_library.utils import RegisterForm


class LoginView(authviews.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        print(form.errors)
        return render(self.request, self.template_name, {'form': form})

class LogoutView(authviews.LogoutView):
    template_name = 'logout.html'


class RegisterView(generic.View):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
