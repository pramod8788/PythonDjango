from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    # print(tasks)
    serialized = TaskSerializer(tasks, many=True)
    # print("\n",serialized)
    # print("\n",serialized.data)
    res = Response(serialized.data)
    # print("\n",res)
    # print("\n",res.data)
    return res


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

@api_view(['POST'])
def login(request):
    data = request.data
    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password, is_active=True)

        if user is not None:
            # login(request, user)
            return Response({"Login": "true"})
        else:
            return Response({"Login": "false"})
    except:
        print("User not found")
        return Response({"Login": "false"})
