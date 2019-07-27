from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db.models import F
from .models import Category, Favorite
from .serializer import CategorySerializer, FavoriteSerializer


# Create your views here.


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request):
        """

        :param request:
        :return: Response ,Status,Json
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'category created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteListCreateView(ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
            """

            :param serializer:
            :return: Response and status
            """
            if serializer.save():
                return Response({'msg': 'favorite created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteView(RetrieveUpdateDestroyAPIView):
    pass
