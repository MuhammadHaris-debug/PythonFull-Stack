from django.urls import path
from .import views

urlpatterns=[
    path('',views.create_students,name='create_students'),
    path('display/',views.display_students,name='display_students'),
]