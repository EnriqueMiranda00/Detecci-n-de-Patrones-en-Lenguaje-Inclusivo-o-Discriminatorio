
from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, change_status
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/change-status/', change_status, name='change_status'),
]
