from django.shortcuts import render

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')


def chat(request):
    return render(request, 'teacher/chat.html')


def calendar(request):
    return render(request, 'teacher/calendar.html')

def setting(request):
    return render(request, 'teacher/setting.html')


def profile(request):
    return render(request, 'teacher/profile.html')

