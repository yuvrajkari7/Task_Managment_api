from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer, TaskAssignmentSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class TaskAssignView(APIView):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            user_ids = serializer.validated_data['user_ids']
            users = User.objects.filter(id__in=user_ids)
            task.assigned_users.set(users)
            task.save()
            return Response({'status': 'task assigned'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)