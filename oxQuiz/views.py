from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OxProblem
from .serializers import OxProblemSerializer
from rest_framework.exceptions import NotFound

class OxProblemList(APIView):
    def get(self, request, format=None):
        problems = OxProblem.objects.all()
        serializer = OxProblemSerializer(problems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OxProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OxProblemDetail(APIView):
    def get_object(self, pk):
        try:
            return OxProblem.objects.get(pk=pk)
        except OxProblem.DoesNotExist:
            raise NotFound('A problem with this ID was not found.')

    def get(self, request, pk, format=None):
        problem = self.get_object(pk)
        serializer = OxProblemSerializer(problem)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        problem = self.get_object(pk)
        serializer = OxProblemSerializer(problem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        problem = self.get_object(pk)
        problem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
