from django.shortcuts import render
from .models import blogPost
from rest_framework.response import Response
from .serializers import blogPostSerializer
from rest_framework.views import APIView


class BlogList(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        if id:
            post = blogPost.objects.get(id=id)
            serializer = blogPostSerializer(post)
            return Response(serializer.data)
        else:
            post = blogPost.objects.all()
            serializer = blogPostSerializer(post, many=True)
            return Response(serializer.data)           
        
    def post(self, request):
        post_data = request.data
        serializer = blogPostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request):
        id = request.query_params.get('id')
        post = blogPost.objects.get(id=id)
        post_data = request.data
        serializer = blogPostSerializer(post, data=post_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request):
        id = request.query_params.get('id')
        post = blogPost.objects.get(id=id)
        post.delete()
        return Response('Post deleted')