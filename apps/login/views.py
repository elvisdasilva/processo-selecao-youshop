from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def HomeView(request):
    return render(request, "home/home.html")


class LoginView(LoginView):
    template_name = "login/login.html"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Dados inválidos")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(LogoutView):
    next_page = reverse_lazy("login")
