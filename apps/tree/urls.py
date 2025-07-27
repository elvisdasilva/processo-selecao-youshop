from django.urls import path

from apps.tree.views import MyPlantedTreeListView, PlantTreeListApiView, PlantedTreeCreateView, PlantedTreeUpdateView, UserAccountsPlantedTreeListView


urlpatterns = [
    path('planted-tree/', MyPlantedTreeListView.as_view(), name='planted_tree_list'),
    path('planted-tree/create/', PlantedTreeCreateView.as_view(), name='planted_tree_create'),
    path('planted-tree/update/<int:pk>/', PlantedTreeUpdateView.as_view(), name='planted_tree_update'),
    path('user-accounts-planted-tree/', UserAccountsPlantedTreeListView.as_view(), name='user_accounts_planted_tree_list'),

    path('api/planted-tree/', PlantTreeListApiView.as_view(), name='planted_tree_api_list'),
]