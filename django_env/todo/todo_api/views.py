# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.auth.models import User
class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetailAptView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id):
        try:
            print(todo_id)
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieve the Todo with given todo_id
        '''
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
        Update the Todo with given todo_id
        '''
        todo = self.get_object(todo_id)
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Delete the Todo with given todo_id
        '''
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class createUser(APIView):
    def post(self, request, *args, **kwargs):
        userName = request.data.get('username')
        Password = request.data.get('password')
        Email = request.data.get('email')
        is_superuser = request.data.get('is_superuser')
        user = User.objects.create_user(username = userName, password=Password,email = Email, is_superuser = is_superuser)
        user.save()
        return Response(status=status.HTTP_201_CREATED)