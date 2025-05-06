from django.urls import path
from . views import QuestionSerializerView, ChoiceSerializerView

urlpatterns = [
    path('my_appQ',QuestionSerializerView.as_view(), name="Question_list"),
    path('my_appC',ChoiceSerializerView.as_view(), name="choice_list"),
]