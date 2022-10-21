from django.urls import path
from . import views
from .views import StudentView

urlpatterns = [
    path('', StudentView.as_view()),

]