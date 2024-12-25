from django.shortcuts import render
from .models import Teacher
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

@login_required
def teacher_profile(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    return render(request, 'teacher/profile.html', {'teacher': teacher})

# Create your views here.
