
from rest_framework import serializers
from .models import User, Author


class AuthorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['is_staff', 'user']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли не совпадают!')
        if len(data['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий!')
        return data


    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
        except Exception as e:
            raise serializers.ValidationError(f'Не удалось создать пользователя {e}')
        else:
            author = Author.objects.create(
                user=user,
                is_staff=validated_data['is_staff'],
                telegram_chat_id=validated_data['telegram_chat_id'],
                email=validated_data['email'],

            )
            return author


