from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student

@api_view(['GET','POST','PUT','PATCH' ,'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
      
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully!!','data':request.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

    if request.method == 'PATCH':
    
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data updated succesfully!!!"})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        
    if request.method == 'DELETE':
        id = pk
        Student.objects.get(pk=id).delete()
        return Response({'msg':'Deleted !!!'})
