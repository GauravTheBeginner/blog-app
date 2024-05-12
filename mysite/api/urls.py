from django.urls import path
from . import views
from .views import (
    BlogList,
)

urlpatterns = [
    path('blogposts/', BlogList.as_view()),
]