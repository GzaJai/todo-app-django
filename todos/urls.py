from django.urls import path
from . import views as v
#from .views import home_view, create_todo_view, todo_details, edit_todo

urlpatterns = [
    path('', v.home_view, name='home'),
    path('todo/create', v.create_todo_view, name='create_todo'),
    path('todo/<int:todo_id>', v.todo_details, name='todo_details'),
    path('todo/edit/<int:todo_id>', v.edit_todo, name='edit_todo'),
    path('todo/delete/<int:todo_id>', v.delete_todo, name='delete_todo'),

]