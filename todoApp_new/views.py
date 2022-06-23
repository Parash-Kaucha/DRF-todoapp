from rest_framework.response import Response
from todoApp.models import ToDo
from .serializers import ToDoSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todo_api(request):
    # API based view function to perform CRUD operation
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            todo = ToDo.objects.get(id=id)
            serializer = ToDoSerializer(todo)
            return Response(serializer.data)
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, content_type='application/json')
        return Response(serializer.errors)

    if request.method == "PUT":
        id = request.data.get('id')
        todo = ToDo.objects.get(id=id)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = request.data.get('id')
        todo = ToDo.objects.get(id=id)
        todo.delete()
        return Response({'msg':'Data Deleted'})
