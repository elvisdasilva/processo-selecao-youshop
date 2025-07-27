from apps.user.views import ProfileView
from django.urls import path

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]
