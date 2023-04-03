from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todo_listsSerializer
from .models import Todo_lists

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = Todo_listsSerializer
    queryset = Todo_lists.objects.all()