from django.urls import path, register_converter

from task import views, converters

register_converter(converters.DateConverter, 'date')

app_name = 'task'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('toggle/<int:pk>/', views.ToggleTaskView.as_view(), name='toggle'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('date/<date:date>/', views.DateTaskListView.as_view(), name='date'),
    path(
        'delete/completed/',
        views.DeleteCompletedTaskView.as_view(),
        name='delete-completed',
    ),
]
