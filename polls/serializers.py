from rest_framework import serializers
from .models import Choice
from .models import Question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id',
        'question',
        'choice_text',
        'votes',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    # Include nested choices in the question response
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
        'id',
        'question_text',
        'pub_date',
        'choices',
        ]
