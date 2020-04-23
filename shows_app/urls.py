from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    # path('edits.html', views.edit),
    path('shows', views.shows),
    path('delete', views.delete),
    path('index.html', views.add),
    path('edit_shows.html', views.goto),
    path('new_shows.html', views.new)
]   
