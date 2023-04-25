from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('posts/', PostView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostRetrieveUpdate.as_view()),

    path('comments/', CommentList.as_view()),
    path('post/<int:post_id>/comment/', CommentListCreate.as_view()),
    path('comment/<int:pk>/', CommentRetrieveUpdate.as_view()),

    path('post/status/', PostStatusList.as_view()),
    path('post/<int:post_id>/status/', PostStatusView.as_view()),
    path('status/<int:pk>/', PostStatusRetrieve.as_view()),

    path('comment/status/', CommentStatusList.as_view()),
    path('comment/<int:comment_id>/status/', CommentStatusView.as_view()),
    path('status/<int:pk>/', CommentStatusRetrieve.as_view()),

]
