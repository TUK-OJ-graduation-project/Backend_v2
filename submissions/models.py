from django.db import models
from django.conf import settings
from CodingProblems.models import CodingProblem

class Submission(models.Model):
    RESULT_CHOICES = [
        ('P', 'Pass'), # Pass all test cases
        ('F', 'Fail'), # none of the test cases passed
        ('E', 'Error'), # Coding errors (runtime, compilation errors...)
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(CodingProblem, related_name='submissions', on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=CodingProblem.LANGUAGE_CHOICES)
    code = models.TextField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)