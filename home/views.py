#from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import TodoSerializer, TimingTodoSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from .models import Todo, TimingTodo

class TodoModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Todo instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'uid'  # Important: use 'uid' (UUIDField) instead of default 'pk'

    # Add authentication and permission classes here
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def timings(self, request, uid=None):
        """
        GET /todos/{uid}/timings/
        List all TimingTodos associated with a specific Todo.
        """
        todo = self.get_object()
        timings = TimingTodo.objects.filter(todo=todo)
        serializer = TimingTodoSerializer(timings, many=True)
        return Response({
            'status': True,
            'message': f'Timing entries for Todo: {todo.todo_title}',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_timing(self, request, uid=None):
        """
        POST /todos/{uid}/add_timing/
        Create a TimingTodo for a specific Todo.
        """
        todo = self.get_object()
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

class HomeView(APIView):
    """
    Handle GET, POST, PATCH on home endpoint.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def _build_response(self, method: str):
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Yes! Django REST Framework is working!',
            'method_called': f'You called {method.upper()} method'
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self._build_response('GET')

    def post(self, request):
        return self._build_response('POST')

    def patch(self, request):
        return self._build_response('PATCH')


class TodoListCreateView(APIView):
    """
    GET - List all Todos
    POST - Create a new Todo
    """
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({
            'status': True,
            'message': 'Todo fetched',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Todo created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': False,
            'message': 'Invalid data',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdateView(APIView):
    """
    PATCH - Update a specific Todo identified by uid
    """

    def patch(self, request, uid):
        todo = get_object_or_404(Todo, uid=uid)
        serializer = TodoSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Todo updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'status': False,
            'message': 'Invalid data',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


#Function-based home view to handle GET, POST, PATCH on home endpoint.

# @api_view(['GET', 'POST', 'PATCH'])
# def home(request):
#     if request.method == 'GET':
#         return Response({
#             'status' : 200,
#             'message': 'Yes! Django rest framework is working !!!',
#             'method_called': 'You called GET method'
#         })
#     elif request.method == 'POST':
#         return Response({
#             'status' : 200,
#             'message': 'Yes! Django rest framework is working !!!',
#             'method_called': 'You called POST method'
#         })
#     elif request.method == 'PATCH':
#         return Response({
#             'status' : 200,
#             'message': 'Yes! Django rest framework is working !!!',
#             'method_called': 'You called PATCH method'
#         })
#     else:
#         return Response({
#             'status' : 400,
#             'message': 'Yes! Django rest framework is working !!!',
#             'method_called': 'You called invalid method'
#         })

#Function-based List and create view to handle GET, POST endpoint.

# @api_view(['GET'])
# def get_todo(request):
#     todo_objs = Todo.objects.all()
#     serializer = TodoSerializer(todo_objs, many = True)

#     return Response({
#                 'status' : True,
#                 'message': 'Todo fetched',
#                 'data': serializer.data
#             })

# @api_view(['POST'])
# def post_todo(request):
#     try:
#         data = request.data
#         serializer = TodoSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status' : True,
#                 'message': 'valid or success data',
#                 'data': serializer.data
#             })
#         return Response({
#                 'status' : False,
#                 'message': 'invalid data',
#                 'data': serializer.errors
#         })
#     except Exception as e:
#         print (e)
#         return Response({
#                 'status' : False,
#                 'message': 'something went wrong !!!'
#         })

#Function-based update view to handle PATCH endpoint.

# @api_view(['PATCH'])
# def patch_todo(request, uid):
#     try:
#         obj = Todo.objects.get(uid=uid)
#         serializer = TodoSerializer(obj, data=request.data, partial=True)      
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': True,
#                 'message': 'Todo updated successfully',
#                 'data': serializer.data
#             })

#         return Response({
#             'status': False,
#             'message': 'Invalid data',
#             'errors': serializer.errors
#         })

#     except Todo.DoesNotExist:
#         return Response({
#             'status': False,
#             'message': 'Todo not found'
#         })

#     except Exception as e:
#         print(e)
#         return Response({
#             'status': False,
#             'message': 'Something went wrong',
#             'data': {}
#         })
