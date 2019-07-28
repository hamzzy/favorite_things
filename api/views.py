from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db.models import F
from .models import Category, Favorite
from .serializer import CategorySerializer, FavoriteSerializer


# Create your views here.


class CategoryListView(ListCreateAPIView):
    """
        class view to create and also get list of category for user
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request):
        """
          create  a new category
        :param request:
        :return: Response ,Status,Json
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'category created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteListCreateView(ListCreateAPIView):
    """
     class view to create and also get list of favorite things
    """
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        """
             save  favorite things into  DB
            :param serializer:
            :return: Response and status
            """
        if serializer.save():
            return Response({'msg': 'favorite created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteView(RetrieveUpdateDestroyAPIView):
    """

    """
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def destroy(self, request, *args,**kwargs):
        instance = self.get_object()

        fav = Favorite.objects.filter(
            category=instance.category,
            ranking__gt=instance.ranking,
        ).update(ranking=F('ranking') - 1)
        if fav:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        """

        :param serializer:
        :return:
        """
        if serializer.save():
            return Response({'msg': 'favorite things updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
