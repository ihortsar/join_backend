from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from task_board.serializers import CategorySerializer, TaskSerializer, UserSerializer
from .models import Category, Task
from django.contrib.auth.models import User


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.save()
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, **kwargs):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        first_name = request.data.get("firstName")
        last_name = request.data.get("lastName")
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            return Response({"message": "User successfully created"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class AllUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)

    def delete(self, request, format=None, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            category_data = serializer.validated_data
            category_name = category_data.get("name")
            existing_category = Category.objects.filter(name=category_name).first()

            if existing_category:
                return JsonResponse({"pk": existing_category.pk})
            else:
                category = serializer.save()
                return JsonResponse({"pk": category.pk})
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        categories = Category.objects.all()
        serialized_categories = CategorySerializer(categories, many=True)
        return Response(serialized_categories.data)


class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
