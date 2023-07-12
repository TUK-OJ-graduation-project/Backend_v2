from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

class CodingProblem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE)
    PYTHON = 'PY'
    JAVA = 'JA'
    JAVASCRIPT = 'JS'

    LANGUAGE_CHOICES = [
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
        (JAVASCRIPT, 'JavaScript'),
    ]
    title = models.CharField(max_length=200) # 문제 제목
    description = models.TextField() # 문제 설명
    restrictions = models.TextField() # 제한 사항
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES) # 언어 선택 목록
    input_format = models.TextField() # input 예시
    output_format = models.TextField() # output 예시
    created_at = models.DateTimeField(auto_now_add=True) # 생성일
    updated_at = models.DateTimeField(auto_now=True) # 수정일
    is_deleted = models.BooleanField(default=False) # 삭제여부

class TestCase(models.Model):
    problem = models.ForeignKey(CodingProblem, related_name='test_cases', on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()