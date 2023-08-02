from django.urls import path
from .views import TaskListView, TaskDetailView, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('token/', obtain_auth_token),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
