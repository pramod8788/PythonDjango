from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from django.template import RequestContext
from .tasks import test_func
from send_mail_app.tasks import send_mails_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.
# def test(request):
#     test_func.delay()
#     return render(request, 'mainapp/index.html')

def send_mails_to_all(request):
    send_mails_func.delay()
    return HttpResponse("All Mails Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=18, minute=58)
    task = PeriodicTask.objects.create(
        crontab=schedule, 
        name='schedule_mail_task_'+'8',
        task='send_mail_app.tasks.send_mails_func', 
        # args=json.dumps([[2, 3]])
        )
    return HttpResponse("Schedule Mail Function")


def home(request):
    return render(request, 'mainapp/index.html', {
        'room_name': "broadcast"
    })

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")