from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Submission
from .serializers import SubmissionSerializer
from CodingProblems.models import CodingProblem
import boto3
import os
import json

class SubmissionList(APIView):
    def get(self, request, format=None):
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Once the submission is saved, trigger the grading process
            submission = serializer.instance
            grading_results = self.grade_submission(submission)
            return Response({**serializer.data, 'grading_results': grading_results}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def grade_submission(self, submission):
        # Fetch the problem and test cases
        problem = CodingProblem.objects.get(pk=submission.problem.id)
        test_cases = list(problem.test_cases.all().values("input", "output"))

        # Your code to convert test_cases into the format required by your Lambda function
        lambda_input = {
            "code": submission.code,
            'function_name': 'solution',
            "test_cases": test_cases
        }

        # Initialize a boto3 client for Lambda
        lambda_client = boto3.client(
            'lambda',
            region_name='ap-northeast-2',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName='judge_function',
            InvocationType='RequestResponse',
            Payload=json.dumps(lambda_input)
        )

        # Get the Lambda output from the response
        lambda_output = json.loads(response['Payload'].read().decode())

        # Update the submission result based on the Lambda output
        if lambda_output['result'] == 'Correct':
            submission.result = 'P'
        elif lambda_output['result'] == 'Incorrect':
            submission.result = 'F'
        else:
            submission.result = 'E'
        submission.save()

        # Return the grading results
        return lambda_output


class SubmissionDetail(APIView):
    def get_object(self, pk):
        try:
            return Submission.objects.get(pk=pk)
        except Submission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        submission = self.get_object(pk)
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
