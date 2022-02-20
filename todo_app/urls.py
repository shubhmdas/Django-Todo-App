from django.contrib import admin
from django.urls import path
from todo.views import index, addTodo, deleteTodo, completeTodo, updateTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('addTodo/', addTodo, name='addTodo'),
    path('deleteTodo/<int:todo_id>', deleteTodo, name='deleteTodo'),
    path('completeTodo/<int:todo_id>', completeTodo, name='completeTodo'),
    path('updateTodo/<int:todo_id>', updateTodo, name='updateTodo'),
]
