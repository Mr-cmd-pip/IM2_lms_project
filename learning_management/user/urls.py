from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('teacher/', include('teacher.urls')),
]