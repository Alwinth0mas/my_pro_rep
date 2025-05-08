from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . models import Question, Choice
from . serializers import QuestionSerializer, ChoiceSerializer

def index(request):
    return render(request, 'my_app/index.html')


class QuestionSerializerView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceSerializerView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer   

# Create your views here.
# manual api creation
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class BookAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
