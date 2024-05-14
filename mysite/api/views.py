from django.shortcuts import render
from .models import BlogPost
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from rest_framework.views import APIView


class BlogList(APIView):
    def get(self, request):
        post = BlogPost.objects.all()
        serializer = BlogPostSerializer(post, many=True)
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
    