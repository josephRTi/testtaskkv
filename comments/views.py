from mptt.managers import TreeManager
from rest_framework import status, generics
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class NoteCreateView(generics.CreateAPIView):
    serializer_class = NoteSerializer


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        queryset = Note.objects.filter(pk=self.kwargs['pk'])
        return queryset


class NotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer


class CommentTreeView(generics.ListAPIView):
    serializer_class = CommentTreeSerializer
    queryset = Comment.objects.viewable()

    def get_queryset(self):
        queryset = Comment.objects.viewable().filter(note=self.kwargs['pk'])
        return queryset


class CommentView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all().filter(note=self.kwargs['pk'])
        return queryset


class CommentAnswerTreeView(generics.ListAPIView):
    serializer_class = CommentTreeSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all().filter(pk=self.kwargs['pk'])

        return queryset


class CommentAnswerView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all().filter(parent=self.kwargs['pk'])

        return queryset
