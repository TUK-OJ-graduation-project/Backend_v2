from django.db import models

class BlankProblem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    blank_answer = models.CharField(max_length=255, help_text="Comma separated answers if there are multiple")

    def __str__(self):
        return self.title
