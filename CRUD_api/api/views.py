from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(requests):
    api_urls = {
        'List': '/product-list/',
        'Detail View':'/product-detail/<int:id>/',
        'Create' : '/product-create/',
        'Update' : '/product-update/<int:id>/',
        'Delete' : '/product-delete/<int:id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def showall(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailview(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def productupdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def productdelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("DELETED SUCCESFULLY")