from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer  # Ensure UserSerializer exists
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()

# UserViewSet for CRUD operations via DefaultRouter
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# RegisterView for user registration
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = request.data.get('role')

        if not email or not role:
            return Response({"error": "Email and role are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email, role=role)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# LoginView for user login
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "username": user.username,
                "email": user.email,
                "role": user.role
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# # CSRF Token View
# def get_csrf_token(request):
#     return Response({"detail": "CSRF token view"})
