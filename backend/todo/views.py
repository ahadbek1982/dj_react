from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


# from rest_framework import generics

# class TodoList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer




# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST'])
# def todolist(request, format=None):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data = request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @csrf_exempt
# def todolist(request):
#     if request.method=='GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer = TodoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


def index(request):
    return HttpResponse('hello world!!!')

