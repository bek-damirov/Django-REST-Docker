from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Post, Comment, PostStatus, CommentStatus, Author
from .serializers import PostSerializers, CommentSerializer, PostStatusSerializer, CommentStatusSerializer
from .permisions import PostPermission


class PostView(generics.ListAPIView):
    """
    Api для просмотра постов,
    просматривать могут все
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostCreateView(generics.ListCreateAPIView):
    """
    API для создания постов,
    создавать могут только зарегистрированные пользователи
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [PostPermission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class PostRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    API для удаления, редактирования, постов,
    могут только владельцы постов
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [PostPermission, ]


class CommentList(generics.ListAPIView):
    """
    API для просмотра всех комментариев,
    могут все
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListCreate(generics.ListCreateAPIView):
    """
    API для создания комментария к постов,
    комментировать могут все
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        user1 = Author.objects.all().first()
        if self.request.user.is_anonymous:
            serializer.save(
                author=user1,
                post_id=self.kwargs.get('post_id')
            )
        else:
            serializer.save(
                author=self.request.user.author,
                post_id=self.kwargs.get('post_id')
            )


class CommentRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    API для удаления, изменения комментариев,
    доступ только у админа
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser, ]


class PostStatusList(generics.ListAPIView):
    """
    API для просмотра всех оценок,
    просматривать могут все
    """
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer


class PostStatusView(generics.ListCreateAPIView):
    """
    API для добавления оценок постам,
    могут только авторизованные пользователи
    """
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer
    permission_classes = [PostPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            post_id=self.kwargs.get('post_id')
            )


class PostStatusRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    API для редактирования постов,
    могут только создатели поста
    """
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer
    permission_classes = [PostPermission, ]


class CommentStatusList(generics.ListAPIView):
    """
    API для просмотра оценок на комментарии,
    просматривать могут все
    """
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer


class CommentStatusView(generics.ListCreateAPIView):
    """
    API для добавления оценок комментариям,
    только авторизованным пользователям
    """
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer
    permission_classes = [PostPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(comment_id=self.kwargs.get('comment_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            comment_id=self.kwargs.get('comment_id')
            )


class CommentStatusRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    API для редактирования оценок,
    доступ для создателей оценки
    """
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer
    permission_classes = [PostPermission, ]
