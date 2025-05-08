from django.urls import path
from . views import QuestionSerializerView, ChoiceSerializerView

urlpatterns = [
    path('api/questions',QuestionSerializerView.as_view(), name="Question_list"),
    path('api/choices/',ChoiceSerializerView.as_view(), name="choice_list"),
]

