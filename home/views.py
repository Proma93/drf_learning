import logging
from .serializers import TodoSerializer, TimingTodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status, viewsets, filters
from .permissions import IsOwnerOrSessionOwner, IsOwnerOfRelatedTodo
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo, TimingTodo
logger = logging.getLogger(__name__)

class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class TodoModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Todo instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPagination
    permission_classes = [IsOwnerOrSessionOwner]
    lookup_field = 'uid'  # Important: use 'uid' (UUIDField) instead of default 'pk'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['is_done']
    search_fields = ['todo_title', 'todo_description']
    ordering_fields = ['created_at', 'todo_title']
    ordering = ['created_at']

    def get_queryset(self):
        user = self.request.user
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.save()
            session_key = self.request.session.session_key

        if user.is_authenticated:
            return Todo.objects.filter(user=user)
        return Todo.objects.filter(session_key=session_key)

    def perform_create(self, serializer):
        user = self.request.user
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.save()
            session_key = self.request.session.session_key

        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save(session_key=session_key)    

    @action(detail=True, methods=['get', 'post'], url_path='timings')
    def handle_specific_todo_timings(self, request, uid=None):
        """
        POST /{uid}/timings/
        Create a TimingTodo for a specific Todo.
        """
        todo = self.get_object()
        if request.method == 'GET':
            timing_todo = TimingTodo.objects.filter(todo=todo)
            serializer = TimingTodoSerializer(timing_todo, many=True)
            return Response({
                'status': True,
                'message': f'Detail of TimingTodo',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            data = request.data.copy()
            data['todo'] = str(todo.uid)
            serializer = TimingTodoSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'TimingTodo created successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)

            return Response({
                'status': False,
                'message': 'Failed to create TimingTodo',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get','patch', 'delete'], url_path='timings/(?P<timing_uid>[^/.]+)')
    def manage_timing(self, request, uid=None, timing_uid=None):
        """
        GET: Retrieve a TimingTodo.
        PATCH: Partially update a TimingTodo.
        DELETE: Delete a TimingTodo.
        """
        todo = self.get_object()    
        try:
            timing = TimingTodo.objects.get(uid=timing_uid, todo=todo)
        except TimingTodo.DoesNotExist:
            return Response({
                'status': False,
                'message': 'TimingTodo not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TimingTodoSerializer(timing)
            return Response({
                'status': True,
                'message': f'Detail of TimingTodo {timing_uid}',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            serializer = TimingTodoSerializer(timing, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': f'TimingTodo {timing_uid} updated successfully.',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                'status': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            timing.delete()
            return Response({
                'status': True,
                'message': f'TimingTodo {timing_uid} deleted successfully.'
            }, status=status.HTTP_204_NO_CONTENT)

class TimingsModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing TimingTodo instances.
    Only allows access to related todos owned by the current user/session.
    """
    queryset = TimingTodo.objects.all()
    serializer_class = TimingTodoSerializer
    permission_classes = [IsOwnerOfRelatedTodo]
    pagination_class = CustomPagination
    lookup_field = 'uid'  # Important: use 'uid' (UUIDField) instead of default 'pk'
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]

    # Exact match filtering
    filterset_fields = ['schedule_date']

    # Search across text fields
    search_fields = ['note']

    # Allow ordering
    ordering_fields = ['schedule_date']

    def get_queryset(self):
        user = self.request.user
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.save()
            session_key = self.request.session.session_key

        if user.is_authenticated:
            return TimingTodo.objects.filter(todo__user=user)
        return TimingTodo.objects.filter(todo__session_key=session_key)