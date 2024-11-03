from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.teacher_dashboard, name='teacher-dashboard'),
    path('chat', views.chat, name='chat'),
    path('calendar', views.calendar, name='calendar'),
    path('setting', views.setting, name='setting'),
    path('profile', views.profile, name='profile'),
]