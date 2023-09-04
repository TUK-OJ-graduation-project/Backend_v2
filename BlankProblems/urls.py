from django.urls import path
from .views import BlankProblemListCreate, BlankProblemRetrieveUpdateDestroy, check_blank_problem_answer

urlpatterns = [
    path('api/v2/blank/', BlankProblemListCreate.as_view(), name='blankproblem-listcreate'),
    path('api/v2/blank/<int:pk>/', BlankProblemRetrieveUpdateDestroy.as_view(), name='blankproblem-retrieveupdatedestroy'),
    path('api/v2/blank/check-answer/<int:pk>/', check_blank_problem_answer, name='blankproblem-check-answer'),
]
