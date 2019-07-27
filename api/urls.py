from django.urls import path

from django.urls import path
from .views import (
    CategoryListView, FavouriteListCreateView
                         )


urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("favorite/", FavouriteListCreateView.as_view(), name="category-list")


]