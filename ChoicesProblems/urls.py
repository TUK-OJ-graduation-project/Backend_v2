from django.urls import path
from .views import MCQProblemView

urlpatterns = [
    path('api/v2/mcq/', MCQProblemView.as_view(), name='mcqproblem-list-create'),
    path('api/v2/mcq/<int:pk>/', MCQProblemView.as_view(), name='mcqproblem-retrieve-update-delete'),
]
