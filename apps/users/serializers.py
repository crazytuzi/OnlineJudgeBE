from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    email = serializers.EmailField(label="邮箱", help_text="邮箱", required=True, allow_blank=False,
                                   validators=[UniqueValidator(queryset=User.objects.all(), message="邮箱已被注册")]
                                   )
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
