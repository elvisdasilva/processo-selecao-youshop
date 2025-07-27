from django.forms import modelformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from apps.tree.forms import PlantedTreeModelForm
from apps.tree.models import PlantedTree
from django.core.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tree.serializers import PlantedTreeSerializer


class PlantTreeListApiView(ListAPIView):
    serializer_class = PlantedTreeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return PlantedTree.objects.filter(user=user).order_by("-planted_at")


@method_decorator(login_required(login_url="login"), name="dispatch")
class MyPlantedTreeListView(ListView):
    model = PlantedTree
    template_name = "planted_tree/planted_tree.html"
    context_object_name = "planted_tree_list"

    def get_queryset(self):
        user = self.request.user
        return PlantedTree.objects.filter(user=user).order_by("-planted_at")


@method_decorator(login_required(login_url="login"), name="dispatch")
class UserAccountsPlantedTreeListView(ListView):
    model = PlantedTree
    template_name = "planted_tree/user_accounts_planted_tree.html"
    context_object_name = "user_accounts_planted_tree_list"

    def get_queryset(self):
        accounts = self.request.user.extension.account.all()
        return (
            PlantedTree.objects.filter(account__in=accounts)
            .order_by("-planted_at")
        )


@method_decorator(login_required(login_url="login"), name="dispatch")
class PlantedTreeUpdateView(UpdateView):
    model = PlantedTree
    template_name = "planted_tree/forms/update_planted_tree.html"
    form_class = PlantedTreeModelForm
    success_url = reverse_lazy("planted_tree_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        planted_tree = self.get_object()
        if planted_tree.user != request.user:
            return HttpResponseForbidden(
                "Você não tem permissão para editar esta plantação."
            )
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.account not in self.request.user.extension.account.all():
            raise PermissionDenied(
                self.request, "Você não tem permissão para editar esta plantação."
            )
        return obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        planted_tree = form.instance
        messages.success(
            self.request, f'Árvore Plantada "{planted_tree}" atualizada com sucesso'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar plantação.")
        return super().form_invalid(form)


@method_decorator(login_required(login_url="login"), name="dispatch")
class PlantedTreeCreateView(View):
    template_name = "planted_tree/forms/new_planted_tree.html"
    success_url = reverse_lazy("planted_tree_list")

    def get(self, request):
        FormSet = modelformset_factory(
            PlantedTree,
            form=PlantedTreeModelForm,
            extra=1,
            can_delete=False,
        )
        formset = FormSet(
            queryset=PlantedTree.objects.none(), form_kwargs={"user": request.user}
        )
        return render(request, self.template_name, {"formset": formset})

    def post(self, request):
        FormSet = modelformset_factory(
            PlantedTree,
            form=PlantedTreeModelForm,
            extra=0,
            can_delete=False,
        )
        formset = FormSet(request.POST, form_kwargs={"user": request.user})
        user_extension = request.user.extension

        if formset.is_valid():
            valid_forms = [form for form in formset if form.cleaned_data]

            if not valid_forms:
                messages.error(request, "Nenhum formulário preenchido.")
                return render(request, self.template_name, {"formset": formset})

            try:
                if len(valid_forms) == 1:
                    data = valid_forms[0].cleaned_data
                    user_extension.plant_tree(
                        tree=data["tree"],
                        account=data["account"],
                        age=data["age"],
                        latitude=data["location_latitude"],
                        longitude=data["location_longitude"],
                    )
                else:
                    tree_data_list = [
                        {
                            "tree": form.cleaned_data["tree"],
                            "account": form.cleaned_data["account"],
                            "age": form.cleaned_data["age"],
                            "latitude": form.cleaned_data["location_latitude"],
                            "longitude": form.cleaned_data["location_longitude"],
                        }
                        for form in valid_forms
                    ]
                    user_extension.plant_trees(tree_data_list)

                messages.success(request, "Árvore(s) plantada(s) com sucesso.")
                return redirect(self.success_url)

            except Exception as e:
                print("Erro ao plantar árvore(s):", e)
                messages.error(request, f"Ocorreu um erro ao plantar árvore(s): {e}")
                return render(request, self.template_name, {"formset": formset})

        for form in formset:
            print(form.errors)

        messages.error(request, "Erro ao cadastrar árvores.")
        return render(request, self.template_name, {"formset": formset})
