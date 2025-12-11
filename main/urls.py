from django.urls import path
from . import views


urlpatterns = [
    # Задачи
    path('', views.tasks_list, name='tasks_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Категории
    path('categories/', views.categories_list, name='categories_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
