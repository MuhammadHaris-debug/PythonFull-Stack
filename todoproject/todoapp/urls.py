from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('complete/<int:id>/', views.complete_task, name='complete'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('edit/<int:id>/', views.edit_task, name='edit'),
]
