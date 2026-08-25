from django.urls import path
from . import views

# URL patterns for the home app.
# The empty path ('') maps to the home view and is named 'home'.
urlpatterns = [
    path('', views.home, name='home'),
    
]