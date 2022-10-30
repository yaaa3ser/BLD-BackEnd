from django.urls import path
from .views import StudentView, StudentDetailView, ParentView, ParentDetailView

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('parents/', ParentView.as_view()),
    path('parents/<int:pk>/', ParentDetailView.as_view()),
]
