from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .models import Category
from .serializer import CategorySerializer
# Create your views here.



class CategoryView(ListCreateAPIView):
    queryset =CategorySerializer

