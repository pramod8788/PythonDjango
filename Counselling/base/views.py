from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import course, follower, applyforcourse
from . forms import courseForm, courseFormEdit, userFormEdit, applyForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    user = request.user
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'home.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password, is_active=True)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password does not match...')
        except:
            messages.error(request, 'User Not Found....')

    return render(request, 'login.html')


def signupPage(request):
    forms = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            if request.user.is_authenticated:
                return redirect('edit-user', pk=user.id)
            else:
                return redirect('home')
        else:
            messages.error(request, "An error occurred! User not Created.")
    context = {"forms":forms,}
    return render(request, 'signup.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def createCourse(request):
    forms = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            courses = form.save(commit=False)
            courses.user = request.user
            courses.save()
            return redirect('home')
    context = {"forms":forms,}
    return render(request, 'createcourse.html', context)


def courseDetails(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    user = request.user
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)
    
    applied_course = applyforcourse.objects.all()

    context = {
        "courses":courses, 
        "mentors":mentors, 
        "students":students,
        "appliedcourse":applied_course,
    }
    return render(request, 'course.html', context)


@login_required(login_url='login')
def editCourse(request, pk):
    data = course.objects.get(id=pk)
    forms = courseFormEdit(instance=data)

    if request.method == 'POST':
        form = courseFormEdit(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"forms":forms, "data":data}
    return render(request, 'createcourse.html', context)


@login_required(login_url='login')
def applyCourse(request):
    if request.method == 'POST':
        user = request.user       
        course_id = request.POST.get('course')
        cor = course.objects.get(course_name=course_id)
        value = request.POST['value']
        if value == "apply":
            follow = applyforcourse.objects.create(user=user, course_id=cor, status=True)
            follow.save()
            return redirect('course')
        else:
            return HttpResponse("Error")


def viewCourse(request,pk):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    user = request.user
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)
    
    data = course.objects.get(id=pk)
    applied_count = applyforcourse.objects.filter(course_id=data)
    applied_course1 = applyforcourse.objects.filter(course_id=data)
    print(applied_course1)

    count = 0
    if len(applied_count) > 0 :
        count = len(applied_count)
    try:
        applied_course = applyforcourse.objects.get(course_id=data, user=request.user)
        context = {
            "courses":courses, 
            "mentors":mentors, 
            "students":students,
            "data":data,
            "applycount":count,
            "appliedcourses":applied_course,
            "appliedcourses1":applied_course1,
        }
    except:
        context = {
            "courses":courses, 
            "mentors":mentors, 
            "students":students,
            "data":data,
            "applycount":count,
            "appliedcourses1":applied_course1,
        }

    return render(request, 'coursedetails.html', context)


def acceptCourse(request,pk):
    data = applyforcourse.objects.get(id=pk)
    forms = applyForm(instance=data)

    if request.method == 'POST':
        form = applyForm(request.POST, instance=data)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {"forms":forms, "data":data}
    return render(request, "coursepermission.html", context)
    

@login_required(login_url='login')
def profile(request):
    user = request.user
    if user.is_superuser:
        courses = course.objects.all()
    else:
        courses = course.objects.filter(user=user)
    mentors = User.objects.filter(groups=1)
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)
    
    applied_course = applyforcourse.objects.filter(user=user)

    following = follower.objects.filter(student=user)
    ment = []
    for i in following:
        ment.append(i.mentor)

    followers = follower.objects.filter(mentor=user)
    stu = []
    for i in followers:
        stu.append(i.student)

    context = {
        "courses":courses, 
        "mentors":mentors, 
        "students":students,
        "appliedCourse":applied_course,
        "followList":ment,
        "followers":stu,
    }
        
    return render(request, 'profile.html', context)


def students(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    user = request.user
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)

    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'students.html', context)


def mentors(request):
    courses = course.objects.all()
    mentors = User.objects.filter(is_staff=True, is_superuser=False)
    students = User.objects.filter(groups=2)
    try:
        followers = follower.objects.filter(student=request.user)
        ment = []
        for i in followers:
            ment.append(i.mentor)
        context = {
            "courses":courses, 
            "mentors":mentors, 
            "students":students, 
            "followers":followers,
            "ment":ment,
        }
    except:
        context = {
            "courses":courses, 
            "mentors":mentors, 
            "students":students,
        }

    return render(request, 'mentors.html', context) 


@login_required(login_url='login')
def editUser(request, pk):
    data = User.objects.get(id=pk)
    forms = userFormEdit(instance=data)

    if request.method == 'POST':
        is_staff = request.POST.get('is_staff')
        mentorToken = request.POST.get('mentor-token')

        form = userFormEdit(request.POST, instance=data)
        if form.is_valid():
            val = form.save(commit=False)
            if is_staff is not None:
                if mentorToken == 'jsdjkvjhkjnkjdndsv':
                    val.save()
                    return redirect('home')
                else:
                    messages.error(request,"Invalid Mentor Token")

    context = {"forms":forms, "data":data}
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        student = request.user       
        mentors = request.POST.get('mentor')
        ment = User.objects.get(username=mentors)
        value = request.POST['value']
        if value == "follow":
            follow = follower.objects.create(mentor=ment, student=student)
            try:
                follow.save()
            except:
                return redirect('mentors')
        else:
            follow = follower.objects.get(mentor=ment, student=student)
            follow.delete()
            return redirect('mentors')             


def viewProfile(request, pk):
    user = User.objects.get(id=pk)
    if user.is_superuser:
        courses = course.objects.all()
    else:
        courses = course.objects.filter(user=user)

    mentors = User.objects.filter(is_staff=True)
    if user.is_superuser:
        students = User.objects.filter(groups=2)
    else:
        followers = follower.objects.filter(mentor=user)
        students = []
        for i in followers:
            stu = User.objects.get(username=i.student)
            students.append(stu)

    applied_course = applyforcourse.objects.filter(user=user)

    following = follower.objects.filter(student=user)
    ment = []
    for i in following:
        ment.append(i.mentor)

    followers = follower.objects.filter(mentor=user)
    stu = []
    for i in followers:
        stu.append(i.student)

    context = {
        "user":user,
        "courses":courses, 
        "mentors":mentors, 
        "students":students,
        "appliedCourse":applied_course,
        "followList":ment,
        "followers":stu,
    }
        
    return render(request, 'profile.html', context)

