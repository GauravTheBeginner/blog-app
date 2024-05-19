from django.shortcuts import render
from .models import BlogPost
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BlogPostFilter
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogList(APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BlogPostFilter
    search_fields = ['title', 'categories']  # Add other fields you want to search

    def get(self, request):
        queryset = BlogPost.objects.all()

        # filters
        filterset = BlogPostFilter(request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs

        # search
        search_filter = SearchFilter()
        queryset = search_filter.filter_queryset(request, queryset, self)

        # ordering
        ordering = request.GET.get('ordering', None)
        if ordering:
            queryset = queryset.order_by(ordering)

        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_data = request.data
        serializer = BlogPostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BlogDetail(APIView):
    def get(self, id):
        post = BlogPost.objects.get(id=id)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    def patch(self, request, id):
        post = BlogPost.objects.get(id=id)
        post_data = request.data
        serializer = BlogPostSerializer(post, data=post_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        post = BlogPost.objects.get(id=id)
        post.delete()
        return Response('Post deleted')
