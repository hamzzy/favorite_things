from django.urls import path

from django.urls import path
from .views import (
           CategoryView
                         )


urlpatterns = [
    path("categories/", CategoryView.as_view(), name="category-list")

]