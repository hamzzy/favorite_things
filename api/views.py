from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category
from .serializer import CategorySerializer


# Create your views here.


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'category created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteView(RetrieveUpdateDestroyAPIView):
    pass
