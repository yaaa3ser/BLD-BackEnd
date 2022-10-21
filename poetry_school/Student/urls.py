from django.urls import path
from . import views
from .views import StudentView , StudentViewParams

urlpatterns = [
    path('', StudentView.as_view()),
    path('<int:pk>', StudentViewParams.as_view()),
]
