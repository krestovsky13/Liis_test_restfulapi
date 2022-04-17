from rest_framework import viewsets
from .serializers import PostSerializer, PostDetailSerializer, ChangePostSerializer
from .models import Post
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ChangePostSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        get_object_or_404(Post, id=pk)
        queryset = Post.objects.filter(id=pk)
        serializer = PostDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.author:
            return Response({
                "detail": "У вас недостаточно прав (Новые статьи могу создавать только авторы)",
            })
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        if not request.user.author:
            return Response({
                "detail": "У вас недостаточно прав (Редактировать статьи могу только авторы)",
            })
        if request.user.id != post.author_id:
            return Response({
                "detail": "Вы можете редактировать только ваши статьи",
            })
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        if not request.user.author:
            return Response({
                "detail": "У вас недостаточно прав (Редактировать статьи могу только авторы)",
            })
        if request.user.id != post.author_id:
            return Response({
                "detail": "Вы можете удалять только ваши статьи",
            })
        return super().destroy(request, pk, *args, **kwargs)
