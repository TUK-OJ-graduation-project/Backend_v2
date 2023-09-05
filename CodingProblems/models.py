from django.db import models
from django.conf import settings
import uuid

class CodingProblem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE)
    PYTHON = 'PY'
    JAVA = 'JA'
    JAVASCRIPT='JS'

    LANGUAGE_CHOICES = [
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
        (JAVASCRIPT, 'JavaScript'),
    ]
    title = models.CharField(max_length=200) # problem title
    description = models.TextField() # Describe the problem
    restrictions = models. TextField() # restrictions
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES) # list of language choices
    input_format = models.TextField() # example input (testcase)
    output_format = models.TextField() # example output (testcase)
    level = models.CharField(max_length=100, default="Level 1")
    hint = models.CharField(max_length=400, default="No Hint")
    created_at = models.DateTimeField(auto_now_add=True) # creation date
    updated_at = models.DateTimeField(auto_now=True) # Modification date
    is_deleted = models.BooleanField(default=False) # Whether to delete

class TestCase(models.Model):
    problem = models.ForeignKey(CodingProblem, related_name='test_cases', on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
