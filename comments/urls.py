from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from .views import *

schema_view = get_swagger_view(title='Comments API')

app_name = 'comments'

urlpatterns = [
    path('note/', NoteCreateView.as_view()),
    path('note/<int:pk>', NoteView.as_view()),
    path('notes/', NotesView.as_view()),
    path('docs/', schema_view),
    path('comment/', CommentCreateView.as_view()),
    path('note_comments_tree/<int:pk>', CommentTreeView.as_view()),
    path('note_comments/<int:pk>', CommentView.as_view()),
    path('answers_to_comment_tree/<int:pk>', CommentAnswerTreeView.as_view()),
    path('answers_to_comment/<int:pk>', CommentAnswerView.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/token', obtain_auth_token, name='token'),
    #
    # path('surveys/delete/<int:pk>', SurveyDeleteView.as_view()),
    # path('surveys/create/', SurveyCreateView.as_view()),
    # path('surveys/update/<int:pk>', SurveyUpdateView.as_view()),
    #
    # path('questions/delete/<int:pk>', QuestionDeleteView.as_view()),
    # path('questions/create/', QuestionCreateView.as_view()),
    # path('questions/update/<int:pk>', QuestionUpdateView.as_view()),
    #
    # path('answers/delete/<int:pk>', AnswerDeleteView.as_view()),
    # path('answers/create/', AnswerCreateView.as_view()),
    # path('answers/update/<int:pk>', AnswerUpdateView.as_view()),
    #
    # path('votefacts/delete/<int:pk>', VoteFactDeleteView.as_view()),
    # path('votefacts/create/', VoteFactCreateView.as_view()),
    # path('votefacts/update/<int:pk>', VoteFactUpdateView.as_view()),
    # path('votefacts/getAll', VoteFactListView.as_view()),

]
