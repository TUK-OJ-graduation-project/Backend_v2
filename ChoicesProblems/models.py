from django.db import models

class MCQProblem(models.Model):
    question_text = models.TextField()

class MCQOption(models.Model):
    problem = models.ForeignKey(MCQProblem, related_name='options', on_delete=models.CASCADE)
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)
