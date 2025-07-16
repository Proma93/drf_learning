from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called POST method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status' : 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called PATCH method'
        })
    else:
        return Response({
            'status' : 400,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called invalid method'
        })
@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many = True)

    return Response({
                'status' : True,
                'message': 'Todo fetched',
                'data': serializer.data
            })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'message': 'valid or success data',
                'data': serializer.data
            })
        return Response({
                'status' : False,
                'message': 'invalid data',
                'data': serializer.errors
        })
    except Exception as e:
        print (e)
        return Response({
                'status' : False,
                'message': 'something went wrong !!!'
        })

@api_view(['PATCH'])
def patch_todo(request, uid):
    try:
        obj = Todo.objects.get(uid=uid)
        serializer = TodoSerializer(obj, data=request.data, partial=True)      
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Todo updated successfully',
                'data': serializer.data
            })

        return Response({
            'status': False,
            'message': 'Invalid data',
            'errors': serializer.errors
        })

    except Todo.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Todo not found'
        })

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong',
            'data': {}
        })
