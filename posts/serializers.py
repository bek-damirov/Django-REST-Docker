from django.db import IntegrityError
from rest_framework import serializers


from .telegram_bot import bot
from .models import Post, Comment, PostStatus, CommentStatus


class PostSerializers(serializers.ModelSerializer):
    average_mark = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['author', 'data_joined']

    def create(self, validated_data):
        user = self.context['request'].user
        chat_id = user.author.telegram_chat_id
        try:
            message = Post.objects.create(**validated_data)
            message.save(
                bot.send_message(chat_id, 'post added')
            )
        except IntegrityError:
            return message


class CommentSerializer(serializers.ModelSerializer):
    average_mark = serializers.ReadOnlyField(source='get_status_com')

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author', 'post', 'data_joined']


class PostStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostStatus
        fields = "__all__"
        read_only_fields = ['author', 'post']


class CommentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentStatus
        fields = "__all__"
        read_only_fields = ['author', 'comment']
