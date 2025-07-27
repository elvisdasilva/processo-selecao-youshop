from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.tree.models import PlantedTree


@login_required(login_url="login")
def HomeView(request):
    user = request.user

    user_tree_count = PlantedTree.objects.filter(user=user).count()
    account_tree_count = PlantedTree.objects.filter(
        account__in=user.extension.account.all()
    ).exclude(user=user).count()

    context = {
        "user_tree_count": user_tree_count,
        "account_tree_count": account_tree_count,
    }

    return render(request, "home/home.html", context=context)


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
