from django.urls import path
from .views import CodingProblemList, CodingProblemDetail, TestCaseView, TestCaseDetail

urlpatterns = [
    path('api/v2/problems/', CodingProblemList.as_view(), name='problem-list'),
    path('api/v2/problems/<uuid:pk>/', CodingProblemDetail.as_view(), name='problem-detail'),
    path('api/v2/problems/<uuid:problem_id>/testcases/', TestCaseView.as_view(), name='testcase-list'),
    path('api/v2/problems/testcases/<int:pk>/', TestCaseDetail.as_view()),
]
