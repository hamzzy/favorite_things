from django.urls import path

from django.urls import path
from .views import (
    CategoryListView, FavouriteListCreateView,FavouriteView
                         )


urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("favorite/", FavouriteListCreateView.as_view(), name="category-list"),
    path("favorite_upcr/<pk>", FavouriteView.as_view(), name="fav_upcr")


]