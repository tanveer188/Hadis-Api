from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import Post
from .serializers import PostDetailSerializer

class PostByDateView(APIView, UserRateThrottle):
  permission_classes = [IsAuthenticated]
  throttle_classes = [UserRateThrottle]

  def get(self, request, date):
    try:
      post = Post.objects.get(date=date)
      serializer = PostDetailSerializer(post)
      print(serializer.get_blocks(post))
      return Response(serializer.data)
    except Post.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
