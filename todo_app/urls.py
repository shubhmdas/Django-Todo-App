from django.contrib import admin
from django.urls import path
from todo.views import index, addTodo, DeleteTodo, completeTodo, UpdateTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('addTodo/', addTodo, name='addTodo'),
    path('deleteTodo/<todo_id>', DeleteTodo.as_view(), name='deleteTodo'),
    path('completeTodo/<todo_id>', completeTodo, name='completeTodo'),
    path('updateTodo/<todo_id>', UpdateTodo.as_view(), name='updateTodo'),
]
