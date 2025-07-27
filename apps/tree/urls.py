from django.urls import path

from apps.tree.views import PlantTreeListApiView, PlantedTreeCreateView, PlantedTreeListView, PlantedTreeUpdateView


urlpatterns = [
    path('planted-tree/', PlantedTreeListView.as_view(), name='planted_tree_list'),
    path('planted-tree/create/', PlantedTreeCreateView.as_view(), name='planted_tree_create'),
    path('planted-tree/update/<int:pk>/', PlantedTreeUpdateView.as_view(), name='planted_tree_update'),

    path('api/planted-tree/', PlantTreeListApiView.as_view(), name='planted_tree_api_list'),
]