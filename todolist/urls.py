from django.urls import path
from . import views

# URL patterns for the todolist app.
# These routes connect the page URLs to the corresponding view functions.
urlpatterns = [
    path("todolist/", views.PostTask, name="todolist"),
    path("todolist/DeleteTask/", views.DeleteTask, name="DeleteTask"),
]