from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('profile/', views.teacher_profile, name='profile'),
]
    
