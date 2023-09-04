from django.urls import path
from .views import QuestionView, AnswerView

urlpatterns = [
    path('api/v2/qna/questions/', QuestionView.as_view()), # 질문 리스트
    path('api/v2/qna/questions/<int:question_id>/', QuestionView.as_view()), # 질문 화면 보기
    path('api/v2/qna/answers/', AnswerView.as_view()), # 답변 리스트
    path('api/v2/qna/answers/<int:answer_id>/', AnswerView.as_view()), # 답변 화면 보기
]