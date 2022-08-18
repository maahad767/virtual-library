from django.shortcuts import render, redirect
from django.contrib.auth import views as authviews
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import RegisterForm


USER_MODEL = get_user_model()

class LoginView(authviews.LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True


class LogoutView(authviews.LogoutView):
    template_name = 'account/logout.html'


class RegisterView(generic.View):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect(self.success_url)
        print(form.errors.as_data())
        return render(request, self.template_name, {'form': form})

class ProfileView(generic.TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
