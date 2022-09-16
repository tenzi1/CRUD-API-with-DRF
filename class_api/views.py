from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import  io
from rest_framework.parsers import JSONParser

from .models import Student
from .serializers import StudentClassSerializer
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentApiView(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentClassSerializer(stu)
            return JsonResponse(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentClassSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentClassSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg':'Data Created'
            }
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentClassSerializer(stu, data = python_data, partial=True) #partial=True for partial update
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg':'Data Updated'
            }
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {
            'msg': 'Data Deleted'
        }
        return JsonResponse(res, safe=False)




