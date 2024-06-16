from django.urls import path
from . import views

urlpatterns = [

    path('todolist/', views.todo_list, name='todo_list'),
    path('todocreatelist/', views.todo_create, name='todo_create'),
    path('tododelete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('complete/<int:id>/', views.todo_complete, name='todo_complete'),
    path('todoupdate/<int:id>/', views.todo_update, name='todo_update'),

]

# m -> v -> t-> u -> u