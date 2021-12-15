from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('logout/', views.logoutPage, name='logout'),

    path('createCourse/', views.createCourse, name='createCourse'),
    path('course/', views.courseDetails, name='course'),
    path('edit-course/<str:pk>/', views.editCourse, name='edit-course'),
    path('apply-course/', views.applyCourse, name='apply-course'),
    path('view-course/<str:pk>/', views.viewCourse, name='view-course'),
    path('accept-course/<str:pk>/', views.acceptCourse, name='accept-course'),

    path('profile/', views.profile, name='profile'),
    path('students/', views.students, name='students'),
    path('mentors/', views.mentors, name='mentors'),
    path('edit-user/<str:pk>/', views.editUser, name='edit-user'),
    path('follow-user/', views.follow, name='follow-user'),
]