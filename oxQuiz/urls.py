from django.urls import path
from .views import OxProblemList, OxProblemDetail

urlpatterns = [
    path('api/v2/ox/list/', OxProblemList.as_view(), name='get_ox_problems'),
    path('api/v2/ox/<int:pk>/', OxProblemDetail.as_view(), name='get_ox_problem_by_id'),
]
