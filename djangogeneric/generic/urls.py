from django.urls import path
from .views import StudentListView,StudentDetailView,StudentUpdateView,StudentDeleteView,StudentCreateView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', StudentDetailView.as_view(),name='student_detail' ),
    path('', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]