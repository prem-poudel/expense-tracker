from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user details.
    """
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        read_only_fields = ("id", "username", "email")


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        min_length=8,
        max_length=128,
    )
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),

        )
        return user
    

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        min_length=8,
        max_length=128,
    )

    def validate(self, attrs):
        username = attrs.get("username", None)
        password = attrs.get("password", None)

        if not username or not password:
            raise serializers.ValidationError({"msg": "Username and password are required."})

        try:
            user: User = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"msg": "User does not exist."})
        
        if user.check_password(password):
            attrs["user"] = user
        else:
            attrs["user"] = None
            raise serializers.ValidationError({"msg": "Incorrect username or password."})

        return attrs


class UserLogoutSerializer(serializers.Serializer):
    """
    Serializer for user logout.
    """
    refresh_token = serializers.CharField(
        max_length=255*2,
        required=True,
        help_text="Refresh token to be blacklisted.",
    )