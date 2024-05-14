from django.urls import path
from . import views
from .views import (
    BlogList,
    BlogDetail
)

urlpatterns = [
    path('blogposts/', BlogList.as_view()),
    path('blogposts/<int:id>/', BlogDetail.as_view()),
]