from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserSerializer,
    UserRegisterSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
)

class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    View to retrieve and update user details.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserRegistrationView(generics.CreateAPIView):
    """
    View to register a new user.
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message": "User registered successfully."
        },
        status=status.HTTP_201_CREATED,
        headers=headers
        )


class UserLoginView(generics.GenericAPIView):
    """
    View to log in a user and obtain JWT tokens.
    """
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.is_active = True  # Ensure user is active
        user.save()
        token = TokenObtainPairSerializer.get_token(user)


        return Response({
            'refresh': str(token),
            'access': str(token.access_token),
            'msg': 'User logged in successfully.',
            'user': UserSerializer(user).data
        }, 
        status=status.HTTP_200_OK
        )


class UserLogoutView(generics.GenericAPIView):
    """
    View to log out a user by blacklisting the refresh token.
    """
    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        refresh_token = serializer.validated_data.get('refresh_token')
        if refresh_token is None:
            return Response(
                {"msg": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST
                )
        token = RefreshToken(refresh_token)
        try:
            token.blacklist()
            user = request.user
            user.is_active = False  # Deactivate user on logout
            user.save()

            return Response(
                {"msg": "User logged out successfully."},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"msg": "An error occurred while logging out."},
                status=status.HTTP_400_BAD_REQUEST
            )
        