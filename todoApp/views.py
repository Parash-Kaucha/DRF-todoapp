from django.http import HttpResponse
from django.http import HttpResponse
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# Class Based View Function
@method_decorator(csrf_exempt, name='dispatch')
class ToDo_API(View):
    def get(self, request, *args, **kwargs):
        python_data = request.GET
        id = python_data.get('id', None)
        if id is not None:
            todo = ToDo.objects.get(id=id)
            serializer = ToDoSerializer(todo) 
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = ToDoSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"New Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        list_id = ToDo.objects.get(id = id)
        serializer = ToDoSerializer(list_id, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        id_data = ToDo.objects.get(id=id)
        id_data.delete()
        res = {'msg':'Data is deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="application/json")
