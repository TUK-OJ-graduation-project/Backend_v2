from django.urls import path
from .views import SubmissionList, SubmissionDetail

urlpatterns = [
    path('api/v2/submissions/', SubmissionList.as_view(), name='submission-list'),
    path('api/v2/submissions/<int:pk>/', SubmissionDetail.as_view(), name='submission-detail'),
]
