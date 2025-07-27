from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib import messages
from apps.user.forms import UserProfileForm
from apps.user.models import UserExtension
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required(login_url="login"), name="dispatch")
class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserExtension
    template_name = "profile/profile.html"
    context_object_name = "profile"
    form_class = UserProfileForm
    login_url = "login"

    def get_object(self, queryset=None):
        return UserExtension.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Perfil atualizado com sucesso.")
        return redirect("profile")

    def form_invalid(self, form):
        print(form.errors)
        messages.error(
            self.request,
            "Erro ao atualizar perfil. Por favor, corrija os erros abaixo.",
        )
        return self.render_to_response(self.get_context_data(form=form))
