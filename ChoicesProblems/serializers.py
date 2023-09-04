from rest_framework import serializers
from .models import MCQProblem, MCQOption

class MCQOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQOption
        fields = ('id', 'option_text', 'is_correct')

class MCQProblemSerializer(serializers.ModelSerializer):
    options = MCQOptionSerializer(many=True)

    class Meta:
        model = MCQProblem
        fields = ('id', 'question_text', 'options')

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        problem = MCQProblem.objects.create(**validated_data)
        for option_data in options_data:
            MCQOption.objects.create(problem=problem, **option_data)
        return problem