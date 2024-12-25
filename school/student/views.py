from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Student

@login_required
def student_profile(request):
    student = get_object_or_404(Student, user=request.user)
    return render(request, 'student/profile.html', {'student': student})
    
# Create your views here.
