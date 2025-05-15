from django.urls import path
from . views import QuestionSerializerView, ChoiceSerializerView
from my_app import views
urlpatterns = [
    path('my_appQ',QuestionSerializerView.as_view(), name="Question_list"),
    path('my_appC',ChoiceSerializerView.as_view(), name="choice_list"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote")
]