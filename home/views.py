from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

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
    
@api_view(['GET', 'POST'])
def post_todo(request):
    try:
        data = request.data
        print(data)
        return Response({
            'status' : True,
            'message': 'success todo created!!!'
    })
    except Exception as e:
        print (e)
        return Response({
                'status' : False,
                'message': 'something went wrong !!!'
        })