from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
	}

	return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serialized = TaskSerializer(tasks, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serialized = TaskSerializer(tasks)
    return Response(serialized.data)


@api_view(['POST'])
def taskCreate(request):
    serialized = TaskSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save()
        return Response("Item Created.")

    return Response(serialized.errors)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serialized = TaskSerializer(instance=task, data=request.data)

    if serialized.is_valid():
        serialized.save()
        return Response("Item Updated.")

    return Response(serialized.errors)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item Deleted.")