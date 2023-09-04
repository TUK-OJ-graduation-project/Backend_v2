from django.db import models

class OxProblem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_correct = models.BooleanField()
    
    def __str__(self):
        return self.title
