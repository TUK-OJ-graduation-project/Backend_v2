from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlankProblem
from .serializers import BlankProblemSerializer

def is_answer_correct(problem, user_answer):
    correct_answers = problem.blank_answer.split(',')
    return user_answer.strip() in correct_answers

class BlankProblemListCreate(generics.ListCreateAPIView):
    queryset = BlankProblem.objects.all()
    serializer_class = BlankProblemSerializer

class BlankProblemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlankProblem.objects.all()
    serializer_class = BlankProblemSerializer

@api_view(['POST'])
def check_blank_problem_answer(request, pk):
    try:
        problem = BlankProblem.objects.get(pk=pk)
    except BlankProblem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user_answer = request.data.get('answer')
    if not user_answer:
        return Response({"error": "Answer not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    if is_answer_correct(problem, user_answer):
        return Response({"correct": True}, status=status.HTTP_200_OK)
    else:
        return Response({"correct": False}, status=status.HTTP_200_OK)
