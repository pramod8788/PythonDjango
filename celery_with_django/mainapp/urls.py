from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.test, name="home"),

    # path('', views.test, name="test"),
    path('send-mails-to-all/', views.send_mails_to_all, name="send-mails-to-all"),
    path('schedule-mail/', views.schedule_mail, name="schedule-mail"),
]
