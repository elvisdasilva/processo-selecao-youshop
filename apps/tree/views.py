from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from apps.tree.forms import PlantedTreeModelForm
from apps.tree.models import PlantedTree


@method_decorator(login_required(login_url="login"), name="dispatch")
class PlantedTreeListView(ListView):
    model = PlantedTree
    template_name = "planted_tree/planted_tree.html"
    context_object_name = "planted_tree_list"


@method_decorator(login_required(login_url="login"), name="dispatch")
class PlantedTreeCreateView(CreateView):
    model = PlantedTree
    template_name = "planted_tree/forms/new_planted_tree.html"
    form_class = PlantedTreeModelForm
    success_url = reverse_lazy("planted_tree_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Árvore plantada com sucesso")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao plantar árvore.")
        return super().form_invalid(form)


@method_decorator(login_required(login_url="login"), name="dispatch")
class PlantedTreeUpdateView(UpdateView):
    model = PlantedTree
    template_name = "planted_tree/forms/update_planted_tree.html"
    form_class = PlantedTreeModelForm
    success_url = reverse_lazy("planted_tree_list")

    def form_valid(self, form):
        planted_tree = form.instance
        messages.success(
            self.request, f'Arvore Plantada "{planted_tree}" atualizada com sucesso'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar plantação.")
        return super().form_invalid(form)
