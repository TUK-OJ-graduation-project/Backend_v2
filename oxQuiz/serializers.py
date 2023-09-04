from rest_framework import serializers
from .models import OxProblem

class OxProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OxProblem
        fields = ['id', 'title', 'description', 'is_correct']
