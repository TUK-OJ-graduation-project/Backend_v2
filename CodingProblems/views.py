from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CodingProblem
from .models import TestCase
from .serializers import TestCaseSerializer
from .serializers import CodingProblemSerializer
from rest_framework.exceptions import NotFound

class CodingProblemList(APIView):
    def get(self, request, format=None):
        problems = CodingProblem.objects.all()
        serializer = CodingProblemSerializer(problems, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CodingProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodingProblemDetail(APIView):
    def get_object(self, pk):
        try:
            return CodingProblem.objects.get(pk=pk)
        except CodingProblem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        problem = self.get_object(pk)
        serializer = CodingProblemSerializer(problem)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        problem = self.get_object(pk)
        serializer = CodingProblemSerializer(problem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        problem = self.get_object(pk)
        problem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TestCaseView(APIView):
    def get(self, request, problem_id, format=None):
        test_cases = TestCase.objects.filter(problem_id=problem_id)
        serializer = TestCaseSerializer(test_cases, many=True)
        return Response(serializer.data)

    def post(self, request, problem_id, format=None):
        serializer = TestCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestCaseDetail(APIView):
    def get_object(self, pk):
        try:
            return TestCase.objects.get(pk=pk)
        except TestCase.DoesNotExist:
            raise NotFound('A test case with this ID was not found.')

    def get(self, request, pk, format=None):
        test_case = self.get_object(pk)
        serializer = TestCaseSerializer(test_case)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        test_case = self.get_object(pk)
        serializer = TestCaseSerializer(test_case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        test_case = self.get_object(pk)
        test_case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)