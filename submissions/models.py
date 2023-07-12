from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from CodingProblems.models import CodingProblem

class Submission(models.Model):
    RESULT_CHOICES = [
        ('P', 'Pass'), # 테스트케이스 전체 통과
        ('F', 'Fail'), # 테스트케이스를 전부 통과 못함
        ('E', 'Error'), # 코딩 자체 에러 (런타임, 컴파일 에러..)
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(CodingProblem, related_name='submissions', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=CodingProblem.LANGUAGE_CHOICES)
    code = models.TextField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

