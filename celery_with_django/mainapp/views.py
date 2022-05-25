from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mails_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

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