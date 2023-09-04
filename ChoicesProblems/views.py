from rest_framework import generics, status
from rest_framework.response import Response
from .models import MCQProblem
from .serializers import MCQProblemSerializer

class MCQProblemView(generics.GenericAPIView):
    queryset = MCQProblem.objects.all()
    serializer_class = MCQProblemSerializer

    def get(self, request, *args, **kwargs):
        mcqproblems = MCQProblem.objects.all()
        serializer = MCQProblemSerializer(mcqproblems, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MCQProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            mcqproblem = MCQProblem.objects.get(pk=kwargs['pk'])
        except MCQProblem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MCQProblemSerializer(mcqproblem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            mcqproblem = MCQProblem.objects.get(pk=kwargs['pk'])
        except MCQProblem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        mcqproblem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
