from rest_framework import serializers
from .models import BlankProblem

class BlankProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProblem
        fields = '__all__'
