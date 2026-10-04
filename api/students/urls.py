from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:id>/', StudentDetail.as_view()),
]
