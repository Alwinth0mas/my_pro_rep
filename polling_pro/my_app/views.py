from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . models import Question, Choice
from . serializers import QuestionSerializer, ChoiceSerializer

# Question “index” page – displays the latest few questions.
# Question “detail” page – displays a question text, with no results but with a form to vote.
# Question “results” page – displays results for a particular question.
# Vote action – handles voting for a particular choice in a particular question.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "my_app/index.html", context)


class QuestionSerializerView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceSerializerView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer   

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "my_app/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse("Your are looking at the result of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("Your are looking at the vote rate of question {}".format(question_id))

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
